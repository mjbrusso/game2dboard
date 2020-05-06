from tkinter import Canvas, PhotoImage
import os, sys

class Cell(Canvas):
    def __init__(self, master):
        self._bg = "red"
        self._image = None
        super().__init__(master, width=200, height=200, bg=self._bg)
        self.pack(pady=10, padx=10)

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
        # TODO: save path
        fname = os.path.dirname(os.path.realpath(sys.argv[0])) + "/" + value
        self._image = PhotoImage(file=fname)
        self.create_image(50, 50, image=self._image)  
