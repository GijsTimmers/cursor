from setuptools import setup
setup(
  name = "cursor",
  packages = ["cursor"],
  version = "1.3.4",
  description = "A small Python package to hide or show the terminal cursor",
  author = "Gijs Timmers",
  author_email = "timmers.gijs@gmail.com",
  url = "https://github.com/GijsTimmers/cursor",
  keywords = ["cursor", "terminal", "hide", "show"],
  classifiers = [],
  entry_points = {
        "console_scripts": ["cursor_hide=cursor:hide",
                            "cursor_show=cursor:show"]}
)
