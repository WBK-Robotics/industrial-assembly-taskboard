# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Industrial Assembly Taskboard'
copyright = '2025, Jan Baumgärtner, Laurin Kreft'
author = 'Jan Baumgärtner, Laurin Kreft'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.napoleon']


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'style_nav_header_background': '#dbe3e6', 'logo_only': True}
html_logo = "images/logo.png"


# -- Options for Latex output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'classoptions': ',dina4,openany',  # Add 'openany' to allow chapters to start on any page
    # Suppress the contents page
    'tableofcontents': '',
    # Add logo to the title page
    'maketitle': r'''
\begin{titlepage}
    \begin{center}
        \vspace*{2cm}
        \includegraphics[width=0.9\textwidth]{logo_with_text.png}\par
        \vspace{1cm}
        {\LARGE Jan Baumgärtner, Laurin Kreft, Alexander Puchta, Jürgen Fleischer \par}
        \vfill
    \end{center}
\end{titlepage}
'''
}
latex_elements['hyperref'] = r'''
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    citecolor=blue,
    pdfborder={0 0 0}
}
'''
