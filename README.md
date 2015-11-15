[![PyPI version](https://badge.fury.io/py/cursor.svg)]
(http://badge.fury.io/py/cursor)

[![Code Health](https://landscape.io/github/GijsTimmers/cursor/master/landscape.svg?style=flat)]
(https://landscape.io/github/GijsTimmers/cursor/master)

# cursor
A small Python package to hide or show the terminal cursor. The code is
compatible with both Python 2 and Python 3.

![demonstration](http://i.imgur.com/2iXviMi.gif)

## Credits
The code is almost entirely a copy of
[James Spencer's]
(http://stackoverflow.com/u/1375885/) 
[answer on StackOverflow]
(http://stackoverflow.com/a/10455937/1096437).

## Installation
The preferred way of installing `cursor` is via `pip`.
You can install `pip` with your package manager:

#### On Ubuntu:
    
    sudo apt-get install python-pip
    sudo pip install cursor

#### On Arch:
    
    sudo pacman -S python-pip
    sudo pip install cursor

## Usage

```python
import cursor
cursor.hide() ## Hides the cursor
cursor.show() ## Shows the cursor
```

Note that the cursor will stay hidden until you call `cursor.show()` — 
even after exiting your python script!

Because of that, `pip` will install two
scripts, which can be run from the command line: `cursor_hide` and
`cursor_show`.
