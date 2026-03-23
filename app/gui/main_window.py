import json
import os
import threading
import traceback
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText

from app.services.xrd_service import PyXploreService, ServiceError

APP_TITLE = 'PyXplore Desktop'
DEFAULTS = {
    'background': {
        'LFctg': '0.5',
        'bac_split': '5',
        'window_length': '17',
        'polyorder': '3',
        'poly_n': '6',
        'mode': 'nearest',
        'bac_var_type': 'constant',
        'model': 'XRD',
    },
    'convert': {
        'target_format': 'csv'
    },
    'xrdfit': {
        'wavelength': '[1.54056, 1.54439]',
        'variance': '1.0',
        'lattice_constants': '[[4.0,4.0,4.0,90,90,90]]',
        'model': 'REFINEMENT',
        'cpu': '4',
        'num': '3'
    }
}


class MainWindow(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master, padding=12)
        self.master = master
        self.service = PyXploreService(self.log)
        self.vars = {}
        self.pack(fill='both', expand=True)
        self._build_ui()

    def _build_ui(self):
        header = ttk.Label(self, text=APP_TITLE, font=('Segoe UI', 18, 'bold'))
        header.pack(anchor='w')
        ttk.Label(
            self,
            text='面向 PyWPEM / PyXplore 的桌面封装。先做三件事：格式转换、背景拟合、XRDfit 主流程。'
        ).pack(anchor='w', pady=(4, 10))

        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)

        notebook.add(self._build_convert_tab(notebook), text='1. 文件转换')
        notebook.add(self._build_background_tab(notebook), text='2. 背景拟合')
        notebook.add(self._build_xrdfit_tab(notebook), text='3. XRD 拟合')

        log_frame = ttk.LabelFrame(self, text='运行日志')
        log_frame.pack(fill='both', expand=True, pady=(10, 0))
        self.log_box = ScrolledText(log_frame, height=14, wrap='word')
        self.log_box.pack(fill='both', expand=True)

        button_row = ttk.Frame(self)
        button_row.pack(fill='x', pady=(8, 0))
        ttk.Button(button_row, text='清空日志', command=lambda: self.log_box.delete('1.0', 'end')).pack(side='left')
        ttk.Button(button_row, text='保存当前配置', command=self.save_config).pack(side='right', padx=(8, 0))
        ttk.Button(button_row, text='读取配置', command=self.load_config).pack(side='right')

    def _build_convert_tab(self, parent):
        frame = ttk.Frame(parent, padding=10)
        self.vars['convert_input'] = tk.StringVar()
        self.vars['convert_output_dir'] = tk.StringVar()
        self.vars['convert_target_format'] = tk.StringVar(value=DEFAULTS['convert']['target_format'])

        self._file_row(frame, '输入文件', self.vars['convert_input'], is_dir=False, row=0)
        self._file_row(frame, '输出目录', self.vars['convert_output_dir'], is_dir=True, row=1)
        self._entry_row(frame, '目标格式', self.vars['convert_target_format'], row=2)
        ttk.Button(frame, text='开始转换', command=self.run_convert).grid(row=3, column=0, columnspan=3, sticky='ew', pady=(12, 0))
        frame.columnconfigure(1, weight=1)
        return frame

    def _build_background_tab(self, parent):
        frame = ttk.Frame(parent, padding=10)
        self.vars['bg_input'] = tk.StringVar()
        self.vars['bg_output_dir'] = tk.StringVar()
        self.vars['bg_lfctg'] = tk.StringVar(value=DEFAULTS['background']['LFctg'])
        self.vars['bg_bac_split'] = tk.StringVar(value=DEFAULTS['background']['bac_split'])
        self.vars['bg_window_length'] = tk.StringVar(value=DEFAULTS['background']['window_length'])
        self.vars['bg_polyorder'] = tk.StringVar(value=DEFAULTS['background']['polyorder'])
        self.vars['bg_poly_n'] = tk.StringVar(value=DEFAULTS['background']['poly_n'])
        self.vars['bg_mode'] = tk.StringVar(value=DEFAULTS['background']['mode'])
        self.vars['bg_bac_var_type'] = tk.StringVar(value=DEFAULTS['background']['bac_var_type'])
        self.vars['bg_model'] = tk.StringVar(value=DEFAULTS['background']['model'])

        self._file_row(frame, '原始强度文件', self.vars['bg_input'], is_dir=False, row=0)
        self._file_row(frame, '输出目录', self.vars['bg_output_dir'], is_dir=True, row=1)
        self._entry_row(frame, 'LFctg', self.vars['bg_lfctg'], row=2)
        self._entry_row(frame, 'bac_split', self.vars['bg_bac_split'], row=3)
        self._entry_row(frame, 'window_length', self.vars['bg_window_length'], row=4)
        self._entry_row(frame, 'polyorder', self.vars['bg_polyorder'], row=5)
        self._entry_row(frame, 'poly_n', self.vars['bg_poly_n'], row=6)
        self._entry_row(frame, 'mode', self.vars['bg_mode'], row=7)
        self._entry_row(frame, 'bac_var_type', self.vars['bg_bac_var_type'], row=8)
        self._entry_row(frame, 'Model', self.vars['bg_model'], row=9)
        ttk.Button(frame, text='开始背景拟合', command=self.run_background).grid(row=10, column=0, columnspan=3, sticky='ew', pady=(12, 0))
        frame.columnconfigure(1, weight=1)
        return frame

    def _build_xrdfit_tab(self, parent):
        frame = ttk.Frame(parent, padding=10)
        self.vars['fit_input_nobg'] = tk.StringVar()
        self.vars['fit_input_original'] = tk.StringVar()
        self.vars['fit_input_background'] = tk.StringVar()
        self.vars['fit_output_dir'] = tk.StringVar()
        self.vars['fit_wavelength'] = tk.StringVar(value=DEFAULTS['xrdfit']['wavelength'])
        self.vars['fit_variance'] = tk.StringVar(value=DEFAULTS['xrdfit']['variance'])
        self.vars['fit_lattice_constants'] = tk.StringVar(value=DEFAULTS['xrdfit']['lattice_constants'])
        self.vars['fit_model'] = tk.StringVar(value=DEFAULTS['xrdfit']['model'])
        self.vars['fit_cpu'] = tk.StringVar(value=DEFAULTS['xrdfit']['cpu'])
        self.vars['fit_num'] = tk.StringVar(value=DEFAULTS['xrdfit']['num'])

        self._file_row(frame, '无背景强度文件', self.vars['fit_input_nobg'], is_dir=False, row=0)
        self._file_row(frame, '原始强度文件', self.vars['fit_input_original'], is_dir=False, row=1)
        self._file_row(frame, '背景文件', self.vars['fit_input_background'], is_dir=False, row=2)
        self._file_row(frame, '输出目录', self.vars['fit_output_dir'], is_dir=True, row=3)
        self._entry_row(frame, 'wavelength(JSON)', self.vars['fit_wavelength'], row=4)
        self._entry_row(frame, 'variance', self.vars['fit_variance'], row=5)
        self._entry_row(frame, 'lattice_constants(JSON)', self.vars['fit_lattice_constants'], row=6)
        self._entry_row(frame, 'MODEL', self.vars['fit_model'], row=7)
        self._entry_row(frame, 'cpu', self.vars['fit_cpu'], row=8)
        self._entry_row(frame, 'num', self.vars['fit_num'], row=9)
        help_label = ttk.Label(
            frame,
            text='说明：这里先封装最常用参数。更复杂的 two_theta_range / density_list / EXACT 等参数可在 xrd_service.py 继续扩展。',
            wraplength=760
        )
        help_label.grid(row=10, column=0, columnspan=3, sticky='w', pady=(4, 0))
        ttk.Button(frame, text='开始 XRD 拟合', command=self.run_xrdfit).grid(row=11, column=0, columnspan=3, sticky='ew', pady=(12, 0))
        frame.columnconfigure(1, weight=1)
        return frame

    def _entry_row(self, parent, label, variable, row):
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky='w', padx=(0, 8), pady=4)
        ttk.Entry(parent, textvariable=variable).grid(row=row, column=1, sticky='ew', pady=4)

    def _file_row(self, parent, label, variable, is_dir, row):
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky='w', padx=(0, 8), pady=4)
        ttk.Entry(parent, textvariable=variable).grid(row=row, column=1, sticky='ew', pady=4)
        cmd = (lambda: self._pick_dir(variable)) if is_dir else (lambda: self._pick_file(variable))
        ttk.Button(parent, text='浏览', command=cmd).grid(row=row, column=2, padx=(8, 0), pady=4)

    def _pick_file(self, variable):
        path = filedialog.askopenfilename()
        if path:
            variable.set(path)

    def _pick_dir(self, variable):
        path = filedialog.askdirectory()
        if path:
            variable.set(path)

    def log(self, message):
        self.log_box.insert('end', f'{message}\n')
        self.log_box.see('end')
        self.master.update_idletasks()

    def _run_async(self, title, target):
        def worker():
            try:
                self.log(f'[{title}] 开始')
                result = target()
                self.log(f'[{title}] 完成: {result}')
                messagebox.showinfo(APP_TITLE, f'{title} 完成')
            except ServiceError as exc:
                self.log(f'[{title}] 失败: {exc}')
                messagebox.showerror(APP_TITLE, str(exc))
            except Exception as exc:
                self.log(f'[{title}] 未知错误: {exc}')
                self.log(traceback.format_exc())
                messagebox.showerror(APP_TITLE, f'{title} 失败\n{exc}')
        threading.Thread(target=worker, daemon=True).start()

    def run_convert(self):
        def target():
            return self.service.convert_file(
                input_file=self.vars['convert_input'].get().strip(),
                output_dir=self.vars['convert_output_dir'].get().strip(),
                target_format=self.vars['convert_target_format'].get().strip(),
            )
        self._run_async('文件转换', target)

    def run_background(self):
        def target():
            return self.service.background_fit(
                intensity_csv=self.vars['bg_input'].get().strip(),
                output_dir=self.vars['bg_output_dir'].get().strip(),
                LFctg=float(self.vars['bg_lfctg'].get().strip()),
                bac_split=int(self.vars['bg_bac_split'].get().strip()),
                window_length=int(self.vars['bg_window_length'].get().strip()),
                polyorder=int(self.vars['bg_polyorder'].get().strip()),
                poly_n=int(self.vars['bg_poly_n'].get().strip()),
                mode=self.vars['bg_mode'].get().strip(),
                bac_var_type=self.vars['bg_bac_var_type'].get().strip(),
                model=self.vars['bg_model'].get().strip(),
            )
        self._run_async('背景拟合', target)

    def run_xrdfit(self):
        def target():
            return self.service.xrdfit(
                no_bac_intensity_file=self.vars['fit_input_nobg'].get().strip(),
                original_file=self.vars['fit_input_original'].get().strip(),
                background_file=self.vars['fit_input_background'].get().strip(),
                output_dir=self.vars['fit_output_dir'].get().strip(),
                wavelength=json.loads(self.vars['fit_wavelength'].get().strip()),
                variance=float(self.vars['fit_variance'].get().strip()),
                lattice_constants=json.loads(self.vars['fit_lattice_constants'].get().strip()),
                model=self.vars['fit_model'].get().strip(),
                cpu=int(self.vars['fit_cpu'].get().strip()),
                num=int(self.vars['fit_num'].get().strip()),
            )
        self._run_async('XRD 拟合', target)

    def save_config(self):
        path = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('JSON', '*.json')])
        if not path:
            return
        data = {k: v.get() for k, v in self.vars.items()}
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        self.log(f'配置已保存: {path}')

    def load_config(self):
        path = filedialog.askopenfilename(filetypes=[('JSON', '*.json')])
        if not path:
            return
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for k, v in data.items():
            if k in self.vars:
                self.vars[k].set(v)
        self.log(f'配置已读取: {path}')


def main():
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry('980x860')
    try:
        root.iconbitmap(default='app_icon.ico')
    except Exception:
        pass
    MainWindow(root)
    root.mainloop()
