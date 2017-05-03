# -*- coding: utf-8 -*-
import sys
import os

try:
    import sphinx_rtd_theme
    RTD_THEME = True
except ImportError:
    RTD_THEME = False

# Add the PyGame-AniSprite repository directory to the module
# search path
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = u'PyGame-AniSprite'
copyright = u'2017, Lily Mayfield'
author = u'Lily Mayfield'

# Read the version information from the PyGame-AniSprite code
init_path = os.path.join(os.path.abspath('..'),
                         'pygame_anisprite',
                         '__init__.py') 

locals = {}
exec(open(init_path).read(),
     {"__name__": "__main__"}, 
     locals)

version = ".".join(locals["__version__"].split(".")[0:2])
release = locals["__version__"]

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
]

# Other Sphinx options
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Output style options
pygments_style = 'sphinx'
html_static_path = ['_static']

html_theme = 'alabaster'
if RTD_THEME:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.4', None),
    'pygame': ('http://www.pygame.org/docs', None),
}
