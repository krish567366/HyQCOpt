# Sphinx configuration
project = 'HyQCOpt'
copyright = '202, Krishna Bajpai'
author = 'Krishna Bajpai'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']