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
    "yasfb",
]
copybutton_prompt_text = ">>> "
myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 6
todo_include_todos = True
toggleprompt_offset_right = 35
feed_base_url = 'https://kasperlin.github.io/AtEoD/'
feed_author = 'Kasper Lin'


# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"
html_title = "AtEoD"
html_last_updated_fmt = "%Y-%m-%d %H:%M"
html_theme_options = {
    "show_toc_level": 1,
    "show_navbar_depth": 1,
    "use_sidenotes": True,
    "navigation_with_keys": False,
}
