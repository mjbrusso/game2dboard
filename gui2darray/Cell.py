from tkinter import *


class Cell(Canvas):
    def __init__(self, master, row, col, size, padx, pady):
        self._image = None  # PhotoImage
        self._value = 0     # this value
        # Canvas constructor:
        super().__init__(
            master,
            width=size[0],
            height=size[1],
            highlightthickness=0)        
        self.grid(row=row, column=col, padx=(padx, 0), pady=(pady, 0))

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
        self.configure(background=self._bg)

    @property
    def image(self):
        """
        Gets or sets the cell image.
        """
        return self._image

    @image.setter
    def image(self, value):
        self.delete("ALL")              # clear Canvas
        w = self.winfo_width() // 2     # horizontal center
        h = self.winfo_height() // 2    # vertical center
        # Show image @ canvas center
        self.create_image(w, h, anchor=CENTER, image=value)
