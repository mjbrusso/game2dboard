import os
import sys
from tkinter import PhotoImage

class ImageMap():
    __imgpath = os.path.dirname(os.path.realpath(sys.argv[0])) + "/img/"

    def __init__(self):
        self._dict = {}

    def __setitem__(self, key, value):
        if not key in self._dict:
            fname = ImageMap.__imgpath + str(value)
            if not os.path.exists(fname):  
                 fname += ".png"            # Is force .png extension a good idea?
            self._dict[key] = PhotoImage(file = fname)

    def __getitem__(self, key):
        if not key in self._dict:
            self[key] = key
        return self._dict[key]
