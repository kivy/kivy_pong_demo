from setuptools import setup, find_packages
from io import open
from os import path

from kivy_pong_demo import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

URL = 'https://github.com/kivy/kivy_pong_demo'

setup(
    name='kivy_pong_demo',
    version=__version__,
    author='Kivy devs',
    license='MIT',
    description='Demo kivy pong-game app.',
    long_description=long_description,
    url=URL,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),
    install_requires=['kivy', 'plyer'],
    extras_require={
        'dev': ['pytest>=3.6', 'pytest-cov', 'flake8', 'sphinx-rtd-theme',
                'trio', 'pytest-trio', 'pyinstaller', 'sphinx',
                'pytest-kivy~=0.1.0.dev1'],
    },
    package_data={'kivy_pong_demo': ['*.kv', '**/*.kv']},
    project_urls={
        'Bug Reports': URL + '/issues',
        'Source': URL,
    },
    entry_points={
        'console_scripts': ['kivy_pong_demo=kivy_pong_demo.main:run']},
)
