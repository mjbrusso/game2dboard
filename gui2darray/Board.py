from tkinter import *
import gui2darray


class Board(Frame):
    def __init__(self, nrows, ncols):
        self._nrows = nrows
        self._ncols = ncols
        self._cells = []
        self._title = "GUI2DArray"
        self._padding = 5
        self._images = gui2darray.ImageMap()
        self._root = Tk()
        super().__init__(self._root)
        self._root.resizable(False, False)
        self.title = self._title

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

    @title.setter
    def padding(self, value):
        self._padding = value

    def run(self):
        self.draw()
        self._root.mainloop()

    def root(self):
        return self._root

    def draw(self):
        for r in range(self._nrows):
            for c in range(self._ncols):
                newcell = gui2darray.Cell(self._root, r, c)
                newcell.image = self._images[12]
                # self._cells.append(newcell)
