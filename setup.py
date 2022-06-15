from setuptools import setup
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = "cursor",
  packages = ["cursor"],
  version = "1.3.5",
  description = "A small Python package to hide or show the terminal cursor",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = "Gijs Timmers",
  author_email = "timmers.gijs@gmail.com",
  url = "https://github.com/GijsTimmers/cursor",
  keywords = ["cursor", "terminal", "hide", "show"],
  classifiers=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
  ],
  entry_points = {
        "console_scripts": ["cursor_hide=cursor:hide",
                            "cursor_show=cursor:show"]}
)
