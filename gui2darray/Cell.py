from tkinter import *


class Cell():
    def __init__(self, parent, x, y, size):
        self._image = None  # PhotoImage
        self._value = 0     # this value
        self._size =  size
        self._parent = parent    
        self._id = parent.create_rectangle(
            x,
            y,
            x+size[0],
            y+size[1],
            width=0
        )

    @property
    def id(self):
        """
        Gets or sets the rectangle id
        """
        return self._id

    @property
    def value(self):
        """
        Gets or sets the cell value.
        """
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @property
    def bg(self):
        """
        Gets or sets the background color.
        """
        return self._bg

    @bg.setter
    def bg(self, value):
        self._bg = value
        self._parent.itemconfig(self._id, fill=value)

    @property
    def image(self):
        """
        Gets or sets the cell image.
        """
        return self._image

    @image.setter
    def image(self, value):
        #self.delete("ALL")              # clear Canvas
        w = self._size[0] // 2     # horizontal center
        h = self._size[1] // 2    # vertical center
        # Show image @ canvas center
        # self.create_image(w, h, anchor=CENTER, image=value)
