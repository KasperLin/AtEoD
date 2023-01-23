# -- Project information -----------------------------------------------------

project = 'AtEoD'
copyright = '2022, kasper'
author = 'kasper'

release = '0.1.0'


# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design", 
    "sphinx_toggleprompt", 
    "sphinx.ext.intersphinx", 
    "sphinx.ext.todo", 
]
copybutton_prompt_text = ">>> "
myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 6
todo_include_todos = True
toggleprompt_offset_right = 35


# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_book_theme'
html_title = "AtEoD"
html_theme_options = {"show_toc_level": 1, "show_navbar_depth": 1}