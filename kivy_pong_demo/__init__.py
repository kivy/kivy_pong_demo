"""Pong Demo
=================

Kivy demo pong app.
"""
import sys
import os
import pathlib

__all__ = ('get_pyinstaller_datas', )

__version__ = '0.2.0.dev0'


def get_pyinstaller_datas():
    """Returns the ``datas`` list required by PyInstaller to be able to package
    :mod:`kivy_pong_demo` in a application.

    """
    root = pathlib.Path(os.path.dirname(sys.modules[__name__].__file__))
    datas = []
    for pat in ('**/*.kv', '*.kv'):
        for f in root.glob(pat):
            datas.append((str(f), str(f.relative_to(root.parent).parent)))

    return datas
