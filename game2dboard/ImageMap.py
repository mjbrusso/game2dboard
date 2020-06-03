import os
import sys
from tkinter import PhotoImage

# A cache to store images

class ImageMap():
    # Singleton Pattern
    __shared_instance = None

    def __init__(self):
        self._dict = {}
        self._imgpath = os.path.dirname(
            os.path.realpath(sys.argv[0])) + "/img/"  # Script path

    @classmethod
    def get_instance(cls):                  # Single instance
        if cls.__shared_instance is None:
            cls.__shared_instance = cls()
        return cls.__shared_instance

    def __setitem__(self, key, value):
        value = str(value)
        if not key in self._dict:
            fname = self._imgpath + value
            if not os.path.exists(fname):
                fname += ".png" 
                if not os.path.exists(fname):
                    self._dict[key] = None
                    return
                
            self._dict[key] = PhotoImage(file=fname)

    def __getitem__(self, key):
        if not key in self._dict:
            self[key] = key
        return self._dict[key]
