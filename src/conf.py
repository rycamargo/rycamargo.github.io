project = 'Raphael Y. de Camargo'
copyright = '2022, Raphael Y. de Camargo'
author = 'Raphael Y. de Camargo <rycamargo@gmail.com>'
html_title = "Raphael Y. de Camargo"
html_logo = "_static/python-logo-generic.svg"

extensions = ["myst_parser"]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']
myst_enable_extensions = ["colon_fence"]

#html_theme = 'alabaster'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

#html_sidebars = {'**': []
#["about.html","navigation.html","relations.html","searchbox.html","donate.html",]
#}

html_sidebars = {"**": ["sidebar-logo.html","sbt-sidebar-nav.html"]}