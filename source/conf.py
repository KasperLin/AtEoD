# -- Project information -----------------------------------------------------

project = "AtEoD"
copyright = "2024, kasper"
author = "kasper"


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
html_theme = "furo"
html_title = "AtEoD"
html_last_updated_fmt = "%Y-%m-%d %H:%M"
html_theme_options = {
    "navigation_with_keys": False,
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]
