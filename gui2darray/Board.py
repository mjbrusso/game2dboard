from tkinter import *
import gui2darray


class Board():
    def __init__(self, nrows, ncols):
        self._isrunning = False
        self._nrows = nrows
        self._ncols = ncols        
        self._cells = []
        self._title = "GUI2DArray"  # Default window title
        self._padding = 5           # grid spacing
        self._bgcolor = "#CCC"      # default background color
        self._cell_size = (50, 50)  # (w, h)
        self._images = gui2darray.ImageMap()
        self._root = Tk()

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
        if self._isrunning:
            raise Exception("Can't update padding after run()")
        self._padding = value
        self._root.configure(padx=self._padding, pady=self._padding)

    @property
    def bgcolor(self):
        """
        Gets or sets the bgcolor.
        """
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, value):
        self._bgcolor = value
        self._root.configure(bg=self._bgcolor)

    @property
    def cell_size(self):
        """
        Gets or sets the cells dimension
        """
        return self._cell_size

    @cell_size.setter
    def cell_size(self, value):
        if self._isrunning:
            raise Exception("Can't resize cells after run()")
        # cell size is a tuple(w, h)
        if not type(value) is tuple:
            v = int(value)
            value = (v, v)
        self._cell_size = value

    def __getitem__(self, x):
        return self._cells[x]
        # https://stackoverflow.com/questions/10727080/how-does-one-override-the-setitem-method-for-possibly-multidimensional-arr

    def run(self):
        self.setupUI()
        self._root.update()
        self._cells[0][0].image = self._images[12]
        self._cells[1][2].image = self._images[16]
        self._isrunning = True

        print(self[0][0].bg)
        self._root.mainloop()

    def root(self):
        return self._root

    def setupUI(self):
        self._root.resizable(False, False)  # Window is not resizable        
        self.bgcolor = self._bgcolor        # Paint background
        self.padding = self._padding        # Change root's padx/y
        self.title = self._title            # Update window's title
        for r in range(self._nrows):
            self._cells.append([])
            pady = r and self._padding      # no y margin in first row (root has top margin)
            for c in range(self._ncols):
                padx = c and self._padding  # no x margin in first collumn (root has left margin)
                newcell = gui2darray.Cell(
                    self._root, r, c, self._cell_size, padx, pady)
                self._cells[r].append(newcell)
