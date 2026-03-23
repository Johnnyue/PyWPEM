@echo off
setlocal
cd /d %~dp0\..

if not exist .venv (
  py -3.10 -m venv .venv
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
if exist requirements.txt (
  python -m pip install -r requirements.txt
)
python -m pip install pyinstaller
python -m PyInstaller packaging\pyinstaller\pyxplore_app.spec --noconfirm --clean

echo.
echo PyInstaller 打包完成。
echo 如需安装器，请用 Inno Setup 打开 packaging\inno\PyXploreSetup.iss 再点 Compile。
endlocal
