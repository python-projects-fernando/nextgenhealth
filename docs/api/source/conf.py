import os
import sys
sys.path.insert(0, os.path.abspath('../../../src'))



project = 'NextGenHealth'
copyright = '2025, Fernando Antunes de Magalhães'
author = 'Fernando Antunes de Magalhães'
release = '0.1.0'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]


templates_path = ['_templates']
exclude_patterns = []


html_theme = 'sphinx_rtd_theme'  # Mude de alabaster para este tema
html_static_path = ['_static']


autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': True,
    'special-members': '__init__',
}