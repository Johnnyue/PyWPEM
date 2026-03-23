import importlib
import os
import shutil
from pathlib import Path


class ServiceError(RuntimeError):
    pass


class PyXploreService:
    def __init__(self, logger=None):
        self.logger = logger or (lambda msg: None)
        self._wpem = None
        self._bacdeduct = None

    def _import_modules(self):
        if self._wpem is None:
            try:
                self._wpem = importlib.import_module('src.WPEM')
            except Exception as exc:
                raise ServiceError(
                    '无法导入 src.WPEM。请确认你已经把本目录合并进 PyWPEM 仓库根目录，并先安装 requirements.txt。'
                ) from exc
        if self._bacdeduct is None:
            try:
                self._bacdeduct = importlib.import_module('src.Background.BacDeduct')
            except Exception as exc:
                raise ServiceError('无法导入 src.Background.BacDeduct。') from exc

    def _ensure_output_dir(self, output_dir):
        if not output_dir:
            raise ServiceError('请先选择输出目录。')
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        return output_dir

    def convert_file(self, input_file, output_dir, target_format='csv'):
        self._import_modules()
        if not input_file or not os.path.isfile(input_file):
            raise ServiceError('输入文件不存在。')
        output_dir = self._ensure_output_dir(output_dir)
        func = getattr(self._bacdeduct, 'convert_file', None)
        if func is None:
            raise ServiceError('源码中未找到 convert_file()。')
        self.logger(f'调用 convert_file: {input_file}')
        try:
            result = func(input_file)
        except TypeError:
            result = func(input_file, target_format)
        # 某些版本 convert_file 直接在原目录生成文件，这里尽量把新文件拷到输出目录
        produced = []
        input_parent = Path(input_file).parent
        stem = Path(input_file).stem
        for p in input_parent.glob(f'{stem}*'):
            if p.is_file() and p.name != Path(input_file).name:
                dest = Path(output_dir) / p.name
                shutil.copy2(p, dest)
                produced.append(str(dest))
        if produced:
            return {'output_files': produced}
        return {'raw_result': str(result), 'note': '未自动识别到新文件，请检查源码转换函数的实际输出位置。'}

    def background_fit(self, intensity_csv, output_dir, LFctg=0.5, bac_split=5,
                       window_length=17, polyorder=3, poly_n=6, mode='nearest',
                       bac_var_type='constant', model='XRD'):
        self._import_modules()
        if not intensity_csv or not os.path.isfile(intensity_csv):
            raise ServiceError('原始强度文件不存在。')
        output_dir = self._ensure_output_dir(output_dir)
        func = getattr(self._wpem, 'BackgroundFit', None)
        if func is None:
            raise ServiceError('源码中未找到 BackgroundFit()。')
        self.logger('调用 BackgroundFit()')
        result = func(
            intensity_csv=intensity_csv,
            LFctg=LFctg,
            bac_split=bac_split,
            window_length=window_length,
            polyorder=polyorder,
            poly_n=poly_n,
            mode=mode,
            bac_var_type=bac_var_type,
            Model=model,
            work_dir=output_dir,
        )
        return {'result': str(result), 'output_dir': output_dir}

    def xrdfit(self, no_bac_intensity_file, original_file, background_file,
               output_dir, wavelength, variance, lattice_constants,
               model='REFINEMENT', cpu=4, num=3):
        self._import_modules()
        for label, path in {
            '无背景强度文件': no_bac_intensity_file,
            '原始强度文件': original_file,
            '背景文件': background_file,
        }.items():
            if not path or not os.path.isfile(path):
                raise ServiceError(f'{label} 不存在。')
        output_dir = self._ensure_output_dir(output_dir)
        func = getattr(self._wpem, 'XRDfit', None)
        if func is None:
            raise ServiceError('源码中未找到 XRDfit()。')
        self.logger('调用 XRDfit()，这一步可能持续较久。')
        result = func(
            wavelength=wavelength,
            Var=variance,
            Lattice_constants=lattice_constants,
            no_bac_intensity_file=no_bac_intensity_file,
            original_file=original_file,
            bacground_file=background_file,
            MODEL=model,
            cpu=cpu,
            num=num,
            work_dir=output_dir,
        )
        return {'result': str(result), 'output_dir': output_dir}
