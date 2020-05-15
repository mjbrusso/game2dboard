from tkinter import *
import gui2darray
import random
from collections import UserList

# TODO: .fill(), .on_mouse_click(), .on_timer(), MessageBar


class Board(UserList):
    def __init__(self, nrows, ncols):
        UserList.__init__(self)             # Initialize parent class
        # Create list [ncols][nrows]
        self.extend([self.BoardRow(ncols, self) for _ in range(nrows)])

        self._isrunning = False
        self._nrows = nrows
        self._ncols = ncols
        # Array used to store cells elements (rectangles)
        self._cells = [[None] * ncols for _ in range(nrows)]
        self._title = "GUI2DArray"            # Default window title
        self._margin = 5                      # board margin (px)
        self._cell_spacing = 1                # grid cell_spacing (px)
        self._margin_color = "light grey"     # default border color
        self._cell_color = "white"            # default cell color
        self._grid_color = "black"            # default grid color
        self._root = Tk()
        # cell's container
        self._canvas = Canvas(self._root, highlightthickness=0)
        # event bindings
        self._on_key_press = None
        self._timer_interval = 0
        self._on_timer = None
        self._root.bind("<Key>", self._key_press)
        #self._root.bind("<ButtonPress>", self._button_down)
        self.cell_size = (50, 50)            # (w, h: px)


    def __getitem__(self, row):           # subscript getter
        self.BoardRow.current_i = row       # Store last accessed row
        return super().__getitem__(row)   # return a BoardRow

    # Properties

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
        self._resize()

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
        # Update bgcolor for all cells
        if self._isrunning:
            for row in self._cells:
                for cell in row:
                    cell.bg = value

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
        return gui2darray.Cell.size

    @cell_size.setter
    def cell_size(self, value):
        if self._isrunning:
            raise Exception("Can't resize cells after run()")
        # size is a tuple (width, height)
        if not type(value) is tuple:
            v = int(value)
            value = (v, v)
        gui2darray.Cell.size = value    # All cells has same size (class field)
        self._resize()

    # Methods

    def run(self):              # Show and start running
        self.setupUI()
        self._isrunning = True
        self._root.mainloop()

    # Random shuffle
    # Copy all values to an array, random.shuffle it, then copy back
    def shuffle(self):
        a = []
        for r in self:
            a.extend(r)
        random.shuffle(a)
        for row in self:
            for c in range(self._ncols):
                row[c] = a.pop()

    # Fill the board (or a row, or a collumn) whith a value
    def fill(self, value, row=None, col=None):
        if row is None and col is None:
            for r in range(self._nrows):
                for c in range(self._ncols):
                    self[r][c] = value
        elif not row is None and col is None:
            for c in range(self._ncols):
                self[row][c] = value
        elif row is None and not col is None:
            for r in range(self._nrows):
                self[r][col] = value
        else:
            raise Exception("Invalid argument supplied (row= AND col=)")

    # Clear board
    def clear(self):
        self.fill(None)

    def _resize(self):
        self._canvas.config(width=self._ncols*(gui2darray.Cell.size[0]+self.cell_spacing)-1,
                            height=self._nrows*(gui2darray.Cell.size[1]+self.cell_spacing)-1)

    # Translate [r][c] to canvas x and y
    def rc2yx(self, row, col):
        y = row*(gui2darray.Cell.size[1]+self.cell_spacing)
        x = col*(gui2darray.Cell.size[0]+self.cell_spacing)
        return (y, x)

    def setupUI(self):
        self._root.resizable(False, False)            # Window is not resizable
        self.margin_color = self._margin_color        # Paint background
        self.grid_color = self._grid_color            # Table inner lines
        self.cell_color = self._cell_color            # Cells background
        self.margin = self._margin                    # Change root's margin
        self.cell_spacing = self._cell_spacing        # Change root's padx/y
        self.title = self._title                      # Update window's title
        # Create all cells
        for r in range(self._nrows):
            for c in range(self._ncols):
                y, x = self.rc2yx(r, c)
                newcell = gui2darray.Cell(self._canvas, x, y)
                newcell.bgcolor = self._cell_color
                self._cells[r][c] = newcell
                if self[r][c] != None:                      # Cell already has a value
                    self.notify_change(r, c, self[r][c])    # show it

        self._canvas.pack()
        self._root.update()

    def close(self):
        self._root.quit()

    # Events

    def notify_change(self, row, col, new_value):
        if self._cells[row][col] != None:
            self._cells[row][col].value = new_value

    # Keyboard events
    @property
    def on_key_press(self):
        return self._on_key_press

    @on_key_press.setter
    def on_key_press(self, value):
        self._on_key_press = value

    def _key_press(self, ev):
        if callable(self.on_key_press):
            self.on_key_press(ev.keysym)

    # Timer events
    @property
    def timer_interval(self):
        return self._timer_interval

    @timer_interval.setter
    def timer_interval(self, value):
        if value != self._timer_interval:       # changed
            self._timer_interval = value            
            if value > 0:
                self._root.after(value, self._timer)

    @property
    def on_timer(self):
        return self._on_timer

    @on_timer.setter
    def on_timer(self, value):
        self._on_timer = value

    def _timer(self):
        intv = self._timer_interval or 0
        if intv > 0:
            if callable(self._on_timer):
                self._on_timer()
            self._root.after(intv, self._timer)

    # Inner class
    # A row is a list, so I can use the magic function __setitem__(board[i][j])
    class BoardRow(UserList):
        # Last acessed row (class member).
        # Yes, its not thread safe!
        # Maybe in the future I will use a proxy class
        current_i = None

        def __init__(self, size, parent):
            UserList.__init__(self)
            self.extend([None] * size)         # Initialize the row
            self._parent = parent           # the board

        def __setitem__(self, j, value):
            self._parent.notify_change(self.__class__.current_i, j, value)
            return super().__setitem__(j, value)
