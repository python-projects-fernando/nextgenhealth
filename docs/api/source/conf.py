# docs/api/source/conf.py
import os
import sys
# Não precisa mais do caminho relativo!
# O pacote já está instalado com pip install -e .

# Project info
project = 'NextGenHealth'
copyright = '2025, Fernando Antunes de Magalhães'
author = 'Fernando Antunes de Magalhães'
release = '0.1.0'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # Para Google/NumPy style docstrings
]

# Templates
templates_path = ['_templates']
exclude_patterns = []

# HTML Theme (MUITO importante!)
html_theme = 'sphinx_rtd_theme'  # Mude de alabaster para este tema
html_static_path = ['_static']

# Autodoc config
autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': True,
    'special-members': '__init__',
}