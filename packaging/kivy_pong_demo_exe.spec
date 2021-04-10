# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
from kivy_deps import sdl2, glew
import kivy_pong_demo
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, \
    get_deps_all, hookspath, runtime_hooks

kwargs = get_deps_minimal(video=None, audio=None, camera=None)
kwargs['hiddenimports'].extend([
    'win32timezone', 'plyer.platforms.win.filechooser',
    'plyer.facades.filechooser', 'kivy.core.window.window_info'])


a = Analysis(['run_app.py'],
             pathex=['.'],
             datas=kivy_pong_demo.get_pyinstaller_datas(),
             hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
             **kwargs)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='PongDemo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='..\\doc\\source\\kivy_pong_demo_logo.ico')
