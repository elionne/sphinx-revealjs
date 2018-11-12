"""Setup module
"""
import re
from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent

with (here / 'README.rst').open(encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'docutils',
    'Sphinx'
]


def fetch_version_string(target: Path) -> str:
    line_re = re.compile(r"__version__ = '(.*?)'", re.S)
    return line_re.search(target.open().read()).group(1)


setup(
    name='sphinx-revealjs',
    version=fetch_version_string(here / 'sphinx_revealjs' / '__init__.py'),
    description='',
    long_description=long_description,
    url='https://gitlab.com/attakei/sphinx-revealjs',
    author='attakei',
    author_email='attakei@gmail.com',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['docs']),
    install_requires=install_requires,
    extras_require={
    },
    include_package_data=True,
)