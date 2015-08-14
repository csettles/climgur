from __future__ import print_function
import time

from six.moves import xrange
from six import add_move, MovedModule
add_move(MovedModule('autopy', 'autopy', 'autopy3'))
from six.moves import autopy


def take_screenshot(filename, delay):
    for i in xrange(1, delay+1):
        time.sleep(1)
        print(i)
    autopy.bitmap.capture_screen().save(filename)
    autopy.alert.alert('A screenshot has been saved.')
