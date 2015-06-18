[![PyPI version](https://badge.fury.io/py/cursor.svg)](https://pypi.python.org/pypi/cursor/0.3)

# cursor
A small Python package to hide or show the terminal cursor.

![demonstration](http://i.imgur.com/2iXviMi.gif)

## Credits
The code is almost entirely a copy of [James Spencer's](http://stackoverflow.com/u/1375885/)
 [answer on StackOverflow](http://stackoverflow.com/a/10455937/1096437).

## Installation
The preferred way of installing `cursor` is via `pip`.
You can install `pip` with your package manager:

#### On Ubuntu:
    
    sudo apt-get install python-pip
    sudo pip install cursor

#### On Arch:
    
    sudo pacman -S python2-pip
    sudo pip2 install cursor

## Usage

```python
import cursor
cursor.hide() ## Hides the cursor
cursor.show() ## Shows the cursor
```

Note that the cursor will stay hidden until you call `cursor.show()` — even after
exiting your python script!