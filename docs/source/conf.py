# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('exts'))

# -- Project information -----------------------------------------------------

project = 'OpenBCI-Stream'
copyright = '2019-2021, Yeison Cardona'
author = 'Yeison Cardona'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',

    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',

    'nbsphinx',
    'sphinx.ext.mathjax',

    'sphinxcontrib.bibtex',
]

naoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'page_width': '1280px',
    'sidebar_width': '300px',

    # 'fixed_sidebar': True,

    # 'show_relbars': True,
    # 'show_relbar_bottom': True,


    # 'github_user': 'bitprophet',
    # 'github_repo': 'alabaster',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    '**': [
        # 'about.html',
        'globaltoc.html',
        # 'navigation.html',
        # 'relations.html',
        # # 'sourcelink.html',
        'searchbox.html',
        # 'donate.html',
    ]
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'OpenBCIdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    # (master_doc, 'OpenBCI.tex', 'OpenBCI Documentation', 'Laura Andrea La Rotta Hurtado', 'manual'),
    (master_doc, 'OpenBCI-Stream.tex',
     'OpenBCI-Stream Documentation', 'Yeison Cardona', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'openbci_stream', 'OpenBCI-Stream Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'OpenBCI-Stream', 'OpenBCI-Stream Documentation',
     author, 'OpenBCI-Stream', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

autodoc_mock_imports = [

    'IPython',
    'numpy',
    'scipy',
    'mne',
    'matplotlib',
    'google',
    'colorama',
    'tqdm',
    'pandas',
    'tables',
    'pyedflib',
    'netifaces',
    'nmap',
    'rawutil',
    'kafka',
    'rpyc',
    'serial',
]

todo_include_todos = True


html_logo = '_static/logo.svg'
html_favicon = '_static/favico.ico'

# autodoc_default_options = [
    # 'members',
    # 'no-undoc-members',
    # 'show-inheritance',
# ]

# autodoc_default_options = {
    # 'members': 'var1, var2',
    # 'member-order': 'bysource',
    # 'special-members': '__init__',
    # 'undoc-members': True,
    # 'exclude-members': '__weakref__'
# }


def setup(app):
    app.add_css_file("custom.css")


highlight_language = 'none'
html_sourcelink_suffix = ''

# nbsphinx_execute_arguments = [
    # "--InlineBackend.figure_formats={'svg', 'pdf'}",
    # "--InlineBackend.rc={'figure.dpi': 96}",
# ]

nbsphinx_execute = 'never'
# nbsphinx_input_prompt = ' '
# nbsphinx_output_prompt = ' '
nbsphinx_kernel_name = 'python3'
nbsphinx_prompt_width = '0'


nbsphinx_prolog = """
.. raw:: html

    <style>
        .nbinput .prompt,
        .nboutput .prompt {
            display: none;
    }
    </style>
"""

notebooks_dir = 'notebooks'

notebooks_list = os.listdir(os.path.join(
    os.path.abspath(os.path.dirname(__file__)), notebooks_dir))
notebooks_list = filter(lambda s: not s.startswith('__'), notebooks_list)

notebooks = []
for notebook in notebooks_list:
    if notebook not in ['readme.ipynb', 'license.ipynb'] and notebook.endswith('.ipynb'):
        notebooks.append(f"{notebooks_dir}/{notebook.replace('.ipynb', '')}")

notebooks = '\n   '.join(sorted(notebooks))

with open('index.rst', 'w') as file:
    file.write(f"""
.. include:: {notebooks_dir}/readme.rst

Navigation
----------

.. toctree::
   :maxdepth: 2
   :name: mastertoc

   {notebooks}


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

    """)


bibtex_bibfiles = ['refs.bib']
