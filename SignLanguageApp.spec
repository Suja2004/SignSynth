# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['expY.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('character/*.glb', 'character'),  # Include all GLB model files
        ('sign_poses.json', '.'),    # Include sign poses data
        ('skybox/*.egg', 'skybox'),  # Include skybox if used
        ('vosk-model-en-us-0.22', 'vosk-model-en-us-0.22'),  # Include Vosk model
    ],
    hiddenimports=[
        'direct.showbase',
        'panda3d.core',
        'direct.gui',
        'direct.task',
        'direct.interval',
        'pyaudio',
        'vosk',
        'nltk',
        'win32com.client',
        'nltk.tokenize',
        'nltk.corpus'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
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
    [],
    exclude_binaries=True,
    name='SignLanguageApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SignLanguageApp',
)