# -- Project information

project = "YATMoS"
copyright = "2022, Pavel Oborin"
author = "Pavel Oborin"

# -- General
extensions = ["myst_parser", "sphinx.ext.autodoc"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- HTML
html_theme = "alabaster"
html_static_path = ["_static"]

# -- autodoc
autodoc_member_order = "bysource"
autodoc_default_flags = ["members"]
autodoc_default_options = {"exclude-members": "__weakref__"}
