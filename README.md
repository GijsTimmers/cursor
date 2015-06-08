# cursor
A small Python package to hide or show the terminal cursor.

## Credits
The code is almost entirely a copy of [James Spencer's](http://stackoverflow.com/u/1375885/)
 [answer on StackOverflow](http://stackoverflow.com/a/10455937/1096437).

## Instalation
The preferred way of installing `cursor` is via `pip`
You can install `pip` via your package manager:

On Ubuntu:
    
    sudo apt-get install python-pip

On Arch:
    
    sudo pacman -S python2-pip
    
Afterwards:

    sudo pip install cursor

## Usage

```python
import cursor
cursor.hide() ## Hides the cursor
cursor.show() ## Shows the cursor
```