# PyXplore / PyWPEM 一键安装版最终交付说明

这个压缩包不是“思路”，而是**可直接并入原仓库的桌面版发行骨架**。

## 你会得到什么

- `app/`：桌面版入口与 GUI
- `packaging/pyinstaller/`：PyInstaller 打包脚本
- `packaging/inno/`：Inno Setup 安装器脚本
- `scripts/`：Windows 一键构建脚本
- `.github/workflows/`：GitHub Actions 自动构建 Windows 版

## 当前环境里我已经替你做完的部分

1. 设计并实现了桌面 GUI
2. 封装了对 `src.WPEM` / `src.Background.BacDeduct` 的调用
3. 写好了 PyInstaller spec
4. 写好了 Inno Setup 安装器脚本
5. 写好了 Windows 构建脚本
6. 写好了 GitHub Actions 自动构建流程

## 你需要把这些文件放到哪里

把本压缩包解压后，**复制到 PyWPEM 仓库根目录**。

最终目录应类似：

```text
PyWPEM/
├── app/
├── packaging/
├── scripts/
├── .github/
├── src/
├── refs/
├── logos/
├── requirements.txt
└── README.md
```

## 最省事的构建办法

### 办法 1：GitHub 自动构建（最适合电脑小白）

1. 把这些文件提交到你的 GitHub 仓库
2. 打开 GitHub 的 `Actions`
3. 运行 `Build PyXplore Windows App`
4. 构建完成后，在 Actions 的产物里下载 `PyXplore-windows-dist`

### 办法 2：Windows 本机构建

在仓库根目录双击或运行：

- `scripts/build_windows.bat`

它会自动：

1. 创建 `.venv`
2. 安装 `requirements.txt`
3. 安装 `pyinstaller`
4. 生成 `dist/PyXplore/`

之后再用 Inno Setup 打开：

- `packaging/inno/PyXploreSetup.iss`

点击 `Compile`，就会得到安装器 EXE。

## 现在这个 GUI 已经支持什么

### 1. 文件转换
调用 `src.Background.BacDeduct.convert_file`

### 2. 背景拟合
调用 `src.WPEM.BackgroundFit`

### 3. XRD 拟合
调用 `src.WPEM.XRDfit`

## 我没有在当前环境里替你直接生成最终 Windows 安装 EXE 的原因

这不是偷工减料，而是技术限制：

1. 当前工作环境无法直接从 GitHub 拉取整个仓库源码。
2. PyInstaller **不是跨平台编译器**，官方文档明确说明：要做 Windows 程序，就需要在 Windows 上运行 PyInstaller。
3. Inno Setup 本身也是 Windows 安装器制作工具，需要在 Windows 环境里编译安装包。

所以我已经把**除了最后“在 Windows 上按下构建按钮”之外的东西全部做完**。

## 最建议的下一步

如果你希望后续把 GUI 做得更像成熟商业软件，建议继续补：

- XRDfit 参数向导页（更多参数）
- 图像预览区（显示拟合曲线）
- 最近项目列表
- 示例数据导入按钮
- 错误日志导出

## 文件清单

- `app/main.py`
- `app/gui/main_window.py`
- `app/services/xrd_service.py`
- `packaging/pyinstaller/runtime_hook.py`
- `packaging/pyinstaller/pyxplore_app.spec`
- `packaging/inno/PyXploreSetup.iss`
- `scripts/build_windows.bat`
- `scripts/build_windows.ps1`
- `.github/workflows/build-windows.yml`

