$ErrorActionPreference = 'Stop'
Set-Location (Join-Path $PSScriptRoot '..')

if (-not (Test-Path '.venv')) {
    py -3.10 -m venv .venv
}
& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
if (Test-Path 'requirements.txt') {
    python -m pip install -r requirements.txt
}
python -m pip install pyinstaller
python -m PyInstaller packaging\pyinstaller\pyxplore_app.spec --noconfirm --clean
Write-Host ''
Write-Host 'PyInstaller 打包完成。'
Write-Host '如需安装器，请用 Inno Setup 打开 packaging\inno\PyXploreSetup.iss 再点 Compile。'
