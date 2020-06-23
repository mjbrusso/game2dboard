import os
import sys
from tkinter import PhotoImage

# A cache to store images

class ImageMap():
    # Singleton Pattern
    __shared_instance = None

    def __init__(self):
        self._dict = {}
        self._imgpath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),  "img") 

    @classmethod
    def get_instance(cls):                  # Single instance
        if cls.__shared_instance is None:
            cls.__shared_instance = cls()
        return cls.__shared_instance

    def load(self, value):
        fname = os.path.join(self._imgpath, value)
        if not os.path.exists(fname):
            fname += ".png"
            if not os.path.exists(fname):
                return None

        return PhotoImage(file=fname)

    def __setitem__(self, key, value):
        value = str(value)
        if not key in self._dict:
            self._dict[key] = self.load(value)

    def __getitem__(self, key):
        if not key in self._dict:
            self[key] = key
        return self._dict[key]
