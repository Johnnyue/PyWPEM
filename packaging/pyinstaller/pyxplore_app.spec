# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules
import os

block_cipher = None
ROOT = Path(os.getcwd()).resolve()

hiddenimports = []
for pkg in [
    'src',
    'src.Background',
    'src.EMBraggOpt',
    'src.Amorphous',
    'src.XRDSimulation',
    'src.Extinction',
    'src.StructureOpt',
    'src.WPEMXPS',
    'src.WPEMXAS',
    'src.GraphStructure',
]:
    try:
        hiddenimports += collect_submodules(pkg)
    except Exception:
        pass

datas = []
for rel in ['refs', 'logos', 'docs', 'CASES']:
    p = ROOT / rel
    if p.exists():
        datas.append((str(p), rel))

a = Analysis(
    [str(ROOT / 'app' / 'main.py')],
    pathex=[str(ROOT)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[str(ROOT / 'packaging' / 'pyinstaller' / 'runtime_hook.py')],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PyXplore',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
