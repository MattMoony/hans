# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import datetime
from typing import *

BPATH: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path = [ BPATH, os.path.join(BPATH, 'hans') ] + sys.path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'hans'
author = 'm4ttm00ny'
release = '0.1.0'
copyright = f'{datetime.datetime.now().year}, {author}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions: List[str] = [ 
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

templates_path: List[str] = [ '_templates', ]
exclude_patterns: List[str] = [ '_build', 'Thumbs.db', '.DS_Store', ]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme: List[str] = 'pydata_sphinx_theme'
html_static_path: List[str] = [ '_static', ]
html_title: str = 'hans'
html_logo: str = '_static/logo.png'
html_favicon: str = '_static/favicon.ico'

html_theme_options:  Dict[str, Any] = {
    'logo': {
        'text': 'hans',
    },
    'github_url': 'https://github.com/MattMoony/hans',
    'navbar_align': 'left',
    'navbar_end': [
        'navbar-icon-links',
        'search-field',
    ],
    'icon_links': [
        {
            'name': 'PyPI',
            'url': 'https://pypi.org/project/hans-cmd/',
            'icon': 'fab fa-python',
        },
    ],
}

html_context: Dict[str, Any] = {
    'github_user': 'MattMoony',
    'github_repo': 'hans',
    'github_version': 'master',
    'doc_path': 'docs',
}
