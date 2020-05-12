from tkinter import *


class Cell():
    def __init__(self, parent, x, y, size):
        self._image = None      # PhotoImage
        self._image_id = None   # tkinter id from create_image
        self._value = 0         # this value
        self._parent = parent  
        self._x = x  
        self._y = y
        self._bgcolor = "white"
        self._size =  size    
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
    def bgcolor(self):
        """
        Gets or sets the background color.
        """
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, value):
        self._bgcolor = value
        self._parent.itemconfig(self._id, fill=value)

    @property
    def image(self):
        """
        Gets or sets the cell image.
        """
        return self._image

    @image.setter
    def image(self, value):        
        if self._image_id:
            self.delete(self._image_id)    # clear current image
        hc = self._x + self.width // 2     # horizontal center
        vc = self._y + self.height // 2    # vertical center
        # Show image @ canvas center
        self._image_id = self._parent.create_image(hc, vc, anchor=CENTER, image=value)

    @property
    def width(self):
         return self._size[0]


    @property
    def height(self):
         return self._size[1]
