# -*- coding: utf-8 -*-
"""Example for stream changing
"""
from __future__ import unicode_literals, absolute_import, print_function
import os
import time
import sys

os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cursor

cursor.hide(stream=sys.stderr)  # Hides the cursor
cursor.show(stream=sys.stderr)  # Shows the cursor

with cursor.HiddenCursor(stream=sys.stderr):  # Cursor will stay hidden
    import time  # while code is being executed;
    for a in range(1, 100):  # afterwards it will show up again
        print(a)
        time.sleep(0.05)
