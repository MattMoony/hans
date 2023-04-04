# -*- coding: utf-8 -*-

import os
from setuptools import setup

BPATH: str = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(BPATH, 'README.md'), 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION: str = f.read()

def version() -> str:
    from hans.__version__ import version
    return version

setup(
    name='hans',
    version=version(),
    author='m4ttm00ny',
    author_email='m4ttm00ny@gmail.com',
    description=(
        'Package for easily building command line interfaces. 🕹️',
    ),
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/MattMoony/hans',
    project_urls={
        'Homepage': 'https://github.com/MattMoony/hans',
        'Documentation': 'https://m4ttm00ny.xyz/hans',
        'Source': 'https://github.com/MattMoony/hans',
        'Tracker': 'https://github.com/MattMoony/hans/issues',
    },
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    packages=[
        'hans',
    ],
    install_requires=[
        'colorama',
        'prompt-toolkit',
        'pyfiglet',
        'rich',
    ],
)
