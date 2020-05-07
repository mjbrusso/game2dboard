from tkinter import *
import gui2darray

class Board():
    def __init__(self, nrows, ncols):
        self._nrows = nrows
        self._ncols = ncols
        self._cells = []
        self._title = "GUI2DArray"
        self._padding = 5
        self._bgcolor = "#CCC"
        self._cell_size = (50, 50)
        self._images = gui2darray.ImageMap()
        self._root = Tk()
        self._root.resizable(False, False)        

    @property
    def title(self):
        """
        Gets or sets the window title.
        """
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self._root.title(self._title)

    @property
    def padding(self):
        """
        Gets or sets the space between cells.
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = value

    @property
    def bgcolor(self):
        """
        Gets or sets the bgcolor.
        """
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, value):
        self._bgcolor = value

    @property
    def cell_size(self):
        """
        Gets or sets the cells dimension
        """
        return self._cell_size

    @cell_size.setter
    def cell_size(self, value):
        if not type(value) is tuple:
            v = int(value)
            value = (v, v)
        self._cell_size = value


    def run(self):
        self.draw()
        self._root.mainloop()

    def root(self):
        return self._root

    def draw(self):
        self._root.configure(bg=self._bgcolor, padx=self._padding, pady=self._padding)
        self.title = self._title
        for r in range(self._nrows):
            for c in range(self._ncols):
                newcell = gui2darray.Cell(self._root, r, c, self._cell_size, self._padding)
                newcell.image = self._images[12]
                # self._cells.append(newcell)
