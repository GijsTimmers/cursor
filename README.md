[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

![PyPI version](https://badge.fury.io/py/cursor.svg)

# cursor 
A small Python package to hide or show the terminal cursor.
Works on Linux and Windows, on both Python 2 and Python 3.

![demonstration](http://i.imgur.com/2iXviMi.gif)

## Disclaimer
The code is almost entirely a copy of
[James Spencer's](http://stackoverflow.com/u/1375885/) 
[answer on StackOverflow](http://stackoverflow.com/a/10455937/1096437).


## Installation
The preferred way of installing `cursor` is via `pip`.
You can install `pip` with your package manager:

#### On Ubuntu:
    
    sudo apt-get install python-pip
    pip install --user cursor

#### On Arch:
    
    git clone https://aur.archlinux.org/python-cursor.git
    cd python-cursor
    makepkg -si

## Usage

```python
import cursor
cursor.hide() ## Hides the cursor
cursor.show() ## Shows the cursor
```


Note that the cursor will stay hidden until you call `cursor.show()` — 
even after exiting your python script!

Because of that, `pip` will install two scripts, which can be run
from the command line: `cursor_hide` and `cursor_show`.

An alternative is using the `HiddenCursor()` class in conjunction
with Python's `with` statement. This will make sure that the cursor
is shown again after running your code, even if exceptions are
raised:

```python
import cursor
with cursor.HiddenCursor():     ## Cursor will stay hidden
    import time                 ## while code is being executed;
    for a in range(1,100):      ## afterwards it will show up again
        print(a)
        time.sleep(0.05)
    
```

You could also use Python's `atexit` module:

```python
import cursor
import atexit
import time

atexit.register(cursor.show)    ## Make sure cursor.show() is called
                                ## when exiting

cursor.hide()                   ## Hides cursor
for a in range(1,100):
    print(a)
    time.sleep(0.05)
exit()                          ## Cursor will show again
```

## Contributors
[Manraj Singh](https://github.com/ManrajGrover): allowed setting
a customisable stream 

[Alexander Seiler](https://github.com/goggle): packaging for Arch

Patrik Kopkan: packaging for Fedora


## Projects using `cursor`
[`halo`](https://github.com/ManrajGrover/halo): beautiful 
terminal spinners in Python

[`pipenv`](https://github.com/pypa/pipenv): a tool that aims to bring the best of all packaging worlds to the Python world

