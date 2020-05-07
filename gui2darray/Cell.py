from tkinter import *

class Cell(Canvas):
    def __init__(self, master, r, c):
        self._bg = "red"
        self._image = None
        super().__init__(master, width=100, height=100, bg=self._bg, bd=0, highlightthickness=0,)
        self.grid(row=r, column=c)

    @property
    def bg(self):
        """
        Gets or sets the background color.
        """
        return self._bg

    @bg.setter
    def bg(self, value):
        self._bg = value
        self.configure(background=self._bg)

    @property
    def image(self):
        """
        Gets or sets the cell image.
        """
        return self._image

    @image.setter
    def image(self, value):
        self.delete("ALL")
        self.create_image(50, 50, image=value)  
