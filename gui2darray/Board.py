from tkinter import *
import gui2darray


class Board(Frame):
    def __init__(self, nrows, ncols):
        self._isrunning = False
        self._nrows = nrows
        self._ncols = ncols
        self._cells = []
        self._title = "GUI2DArray"            # Default window title
        self._margin = 5                      # board margin (px)
        self._cell_spacing = 3                # grid cell_spacing (px)
        self._margin_color = "light grey"     # default border color
        self._cell_color = "white"            # default cell color
        self._grid_color = "black"            # default grid color        
        self._cell_size = (50, 50)            # (w, h: px)
        self._images = gui2darray.ImageMap()
        self._root = Tk()
        self._canvas = Canvas(self._root, highlightthickness=0)       # cell's container

    @property
    def title(self):
        """
        Gets or sets the window title.
        """
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self._root.title(value)

    @property
    def margin(self):
        """
        Gets or sets the board margin.
        """
        return self._margin

    @margin.setter
    def margin(self, value):
        if self._isrunning:
            raise Exception("Can't update margin after run()")
        self._margin = value
        self._root.configure(padx=value, pady=value)

    @property
    def cell_spacing(self):
        """
        Gets or sets the space between cells.
        """
        return self._cell_spacing

    @cell_spacing.setter
    def cell_spacing(self, value):
        if self._isrunning:
            raise Exception("Can't update cell_spacing after run()")
        self._cell_spacing = value
        self.resize()

    @property
    def margin_color(self):
        """
        Gets or sets the margin_color.
        """
        return self._margin_color

    @margin_color.setter
    def margin_color(self, value):
        self._margin_color = value
        self._root.configure(bg=value)

    @property
    def cell_color(self):
        """
        Gets or sets cells color
        """
        return self._cell_color

    @cell_color.setter
    def cell_color(self, value):
        self._cell_color = value
        for c in self._cells:
            c.bg = value

    @property
    def grid_color(self):
        """
        Gets or sets grid color
        """
        return self._grid_color

    @grid_color.setter
    def grid_color(self, value):
        self._grid_color = value
        self._canvas.configure(bg=value)


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
        self.resize()

    def __getitem__(self, x):
        return self._cells[x]
        # https://stackoverflow.com/questions/10727080/how-does-one-override-the-setitem-method-for-possibly-multidimensional-arr

    def run(self):
        self.setupUI()
        self._canvas.pack()
        self._root.update()
        #self._cells[0][0].image = self._images[12]
        # self._cells[1][2].image = self._images[16]
        self._isrunning = True
        self._root.mainloop()

    def root(self):
        return self._root

    def resize(self):
        self._canvas.config(width=self._ncols*(self.cell_size[0]+self.cell_spacing)-1,
                            height=self._nrows*(self.cell_size[1]+self.cell_spacing)-1)

    def setupUI(self):
        self._root.resizable(False, False)            # Window is not resizable
        self.margin_color = self._margin_color        # Paint background
        self.grid_color = self._grid_color
        self.cell_color = self._cell_color
        self.margin = self._margin                    # Change root's margin
        self.cell_spacing = self._cell_spacing        # Change root's padx/y
        self.title = self._title                      # Update window's title
        for r in range(self._nrows):
            self._cells.append([])
            # no y margin in first row (root has top margin)
            pady = r and self._cell_spacing
            for c in range(self._ncols):
                # no x margin in first collumn (root has left margin)
                padx = c and self._cell_spacing
                #newcell = gui2darray.Cell(
                #    self._canvas, r, c, self._cell_size, padx, pady)
                #newcell.bg = self.cell_color
                x = c*(self.cell_size[0]+self.cell_spacing)
                y = r*(self.cell_size[1]+self.cell_spacing)
                newcell = gui2darray.Cell(self._canvas, x, y, self.cell_size)
                newcell.bg = self._cell_color
                self._cells[r].append(newcell)
