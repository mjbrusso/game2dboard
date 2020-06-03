from tkinter import *
import game2dboard
import random
from collections import UserList

# TODO:
#       rezize(r, c), self[i] = [...], beep(), play_sound(), ...


class Board(UserList):
    """
    A graphical user interface for 2d arrays (matrix)
    """

    def __init__(
            self,
            nrows,
            ncols):
        """

        Creates an App

        :param int nrows:
            The number of rows.

        :param int ncols:
            The number of columns.
        """

        UserList.__init__(self)             # Initialize parent class
        # Create list [ncols][nrows]
        self.extend([self._BoardRow(ncols, self) for _ in range(nrows)])

        self._nrows = nrows
        self._ncols = ncols
        self._isrunning = False
        # Array used to store cells elements (rectangles)
        self._cells = [[None] * ncols for _ in range(nrows)]
        self._title = "game2dboard"           # Default window title
        self._cursor = "arrow"                # Default mouse cursor
        self._margin = 5                      # board margin (px)
        self._cell_spacing = 1                # grid cell_spacing (px)
        self._margin_color = "light grey"     # default border color
        self._cell_color = "white"            # default cell color
        self._grid_color = "black"            # default grid color
        self._root = Tk()
        # cell's container
        self._canvas = Canvas(self._root, highlightthickness=0)
        # event bindings
        self._on_key_press = None           # user key press callback
        self._on_mouse_click = None         # user mouse callback
        self._timer_interval = 0            # ms
        self._on_timer = None               # user timer callback
        self._after_id = None               # current timer id
        self._is_in_timer_calback = False
        # register internal key callback
        self._root.bind("<Key>", self._key_press_clbk)
        # register internal mouse callback
        self._canvas.bind("<ButtonPress>", self._mouse_click_clbk)
        self._msgbar = None                 # message bar component

    def __getitem__(self, row):             # subscript getter: self[row]
        # Store last accessed row (NOT thread safe... )
        self._BoardRow.current_i = row
        return super().__getitem__(row)     # return a _BoardRow

    # Properties
    # ---------------------------------------------------------------

    @property
    def size(self):
        """

        Number of elements in the array (readonly).

        :type: int
        """
        return self._nrows * self._ncols

    @property
    def nrows(self):
        """

        Number of rows in the array (readonly).

        :type: int
        """
        return self._nrows

    @property
    def ncols(self):
        """

        Number of columns in the array (readonly).

        :type: int
        """
        return self._ncols

    @property
    def title(self):
        """

        Gets or sets the window title.

        :type: str
        """
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self._root.title(value)

    @property
    def cursor(self):
        """

        Gets or sets the mouse cursor shape.<br>
        Setting to None hides the cursor.

        :type: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        self._cursor = value
        if value is None:
            value = "none"
        self._canvas.configure(cursor=value)

    @property
    def margin(self):
        """

        Gets or sets the board margin (px).

        :type: int
        """
        return self._margin

    @margin.setter
    def margin(self, value):
        if self._isrunning:
            raise Exception("Can't update margin after show()")
        self._margin = value
        self._root.configure(padx=value, pady=value)

    @property
    def cell_spacing(self):
        """
        Gets or sets the space between cells (px).

        :type: int
        """
        return self._cell_spacing

    @cell_spacing.setter
    def cell_spacing(self, value):
        if self._isrunning:
            raise Exception("Can't update cell_spacing after show()")
        self._cell_spacing = value
        self._resize()

    @property
    def margin_color(self):
        """
        Gets or sets the margin_color.

        :type: str
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

        :type: str
        """
        return self._cell_color

    @cell_color.setter
    def cell_color(self, value):
        self._cell_color = value
        # Update bgcolor for all cells
        if self._isrunning:
            for row in self._cells:
                for cell in row:
                    cell.bgcolor = value

    @property
    def grid_color(self):
        """
        Gets or sets grid color

        :type: str
        """
        return self._grid_color

    @grid_color.setter
    def grid_color(self, value):
        self._grid_color = value
        self._canvas.configure(bg=value)

    @property
    def cell_size(self):
        """
        Gets or sets the cells dimension (width, height)

        :type: int or (int, int)
        """
        return game2dboard.Cell.size

    @cell_size.setter
    def cell_size(self, value):
        if self._isrunning:
            raise Exception("Can't resize cells after run()")
        # size is a tuple (width, height)
        if not type(value) is tuple:
            v = int(value)
            value = (v, v)
        # All cells has same size (class field)
        game2dboard.Cell.size = value
        self._resize()

    # Events
    # ---------------------------------------------------------------

    # Keyboard events
    @property
    def on_key_press(self):
        """
        Gets or sets the keyboard callback function

        :type: function(key: str)
        """
        return self._on_key_press

    @on_key_press.setter
    def on_key_press(self, value):
        self._on_key_press = value

    # Internal callback
    def _key_press_clbk(self, ev):
        if callable(self._on_key_press):
            self._on_key_press(ev.keysym)

    # Mouse click events
    @property
    def on_mouse_click(self):
        """
        Gets or sets the mouse callback function

        :type: function(button: str, row: int, col: int)
        """
        return self._on_mouse_click

    @on_mouse_click.setter
    def on_mouse_click(self, value):
        self._on_mouse_click = value

    # Internal callback
    def _mouse_click_clbk(self, ev):
        if callable(self._on_mouse_click):
            rc = self._xy2rc(ev.x, ev.y)
            if rc:
                self._on_mouse_click(ev.num, rc[0], rc[1])

    # Timer events
    @property
    def on_timer(self):
        """
        Gets or sets the timer callback function

        :type: function
        """
        return self._on_timer

    @on_timer.setter
    def on_timer(self, value):
        self._on_timer = value

    # internal callback
    def _timer_clbk(self):
        if self._timer_interval > 0 and callable(self._on_timer):
            self._is_in_timer_calback = True
            self._on_timer()              # Call the user callback function
            self._is_in_timer_calback = False
        if self._timer_interval > 0:      # User callback function may change timer!
            self._after_id = self._root.after(
                self._timer_interval, self._timer_clbk)

    # Methods
    # ---------------------------------------------------------------

    def show(self):
        """

        Create the GUI, display and enter the run loop.

        """
        self._setupUI()
        self._isrunning = True
        self._root.mainloop()

    def clear(self):
        """

        Clear the board, setting all values to None.
        """
        self.fill(None)

    def close(self):
        """

        Close the board, exiting the program.
        """
        self._root.quit()
        self._root.update()

    def create_output(self, **kwargs):
        """

        Create a output message bar.
        kwargs:
            color = str
            background_color` = str
            font_size = int
        """
        if self._msgbar is None:
            self._msgbar = game2dboard.OutputBar(self._root, **kwargs)

    def print(self, *objects, sep=' ', end=''):
        """

        Print message to output bar.
        Use like standard print() function.
        """
        if self._msgbar:
            s = sep.join(str(obj) for obj in objects) + end
            self._msgbar.show(s)

    def shuffle(self):
        """

        Random shuffle all values in the board
        """

        # Copy all values to an array, random.shuffle it, then copy back
        a = []
        for r in self:
            a.extend(r)
        random.shuffle(a)
        for row in self:
            for c in range(self._ncols):
                row[c] = a.pop()

    def fill(self, value, row=None, col=None):
        """

        Fill the board (or a row, or a column) with a value

        :param value: The value to store
        :param int row: Index of row to fill. Default=None (all rows)
        :param int col: Index of column to fill. Default=None (all columns)
        """
        if row is None and col is None:         # all rows and columns
            for r in range(self._nrows):
                for c in range(self._ncols):
                    self[r][c] = value
        elif not row is None and col is None:  # single row
            for c in range(self._ncols):
                self[row][c] = value
        elif row is None and not col is None:   # a single collumn
            for r in range(self._nrows):
                self[r][col] = value
        else:
            raise Exception("Invalid argument supplied (row= AND col=)")


    def start_timer(self, msecs):
        """

        Start a periodic timer that executes the a function every msecs milliseconds

        The callback function must be registered using .on_timer property.

        :param int msecs: Time in milliseconds.
        """
        if msecs != self._timer_interval:                       # changed
            self.stop_timer()
            self._timer_interval = msecs
            if msecs > 0 and not self._is_in_timer_calback:
                self._after_id = self._root.after(msecs, self._timer_clbk)


    def stop_timer(self):
        """

        Stops the current timer.
        """
        self._timer_interval = 0
        if self._after_id:
            self._root.after_cancel(self._after_id)
            self._after_id = None

    def pause(self, msecs, change_cursor=True):
        """

        Delay the program execution for a given number of milliseconds.  
        
        Warning: long pause freezes the GUI!

        :param int msecs: Time in milliseconds.
        :param bool change_cursor: Change the cursor to "watch" during pause?
        """
        if change_cursor:
            oldc = self.cursor
            self.cursor = "watch"
        self._root.update_idletasks()
        self._root.after(msecs)
        if change_cursor:
            self.cursor = oldc

    # Internal functions
    # ---------------------------------------------------------------

    def _setupUI(self):
        self._root.resizable(False, False)            # Window is not resizable
        self.margin_color = self._margin_color        # Paint background
        self.grid_color = self._grid_color            # Table inner lines
        self.cell_color = self._cell_color            # Cells background
        self.margin = self._margin                    # Change root's margin
        self.cell_spacing = self._cell_spacing        # Change root's padx/y
        self.title = self._title                      # Update window's title
        self.cursor = self._cursor
        # Create all cells
        for r in range(self._nrows):
            for c in range(self._ncols):
                x, y = self._rc2xy(r, c)
                newcell = game2dboard.Cell(self._canvas, x, y)
                newcell.bgcolor = self._cell_color
                self._cells[r][c] = newcell
                if self[r][c] != None:                       # Cell has a value
                    self._notify_change(r, c, self[r][c])    # show it

        self._canvas.pack()
        self._root.update()

    def _notify_change(self, row, col, new_value):
        if self._cells[row][col] != None:
            self._cells[row][col].value = new_value

    # Config the canvas size
    def _resize(self):
        self._canvas.config(width=self._ncols*(game2dboard.Cell.width+self.cell_spacing)-self.cell_spacing,
                            height=self._nrows*(game2dboard.Cell.height+self.cell_spacing)-self.cell_spacing)

    # Translate [row][col] to canvas coordinates
    def _rc2xy(self, row, col):
        x = col*(game2dboard.Cell.width+self.cell_spacing)
        y = row*(game2dboard.Cell.height+self.cell_spacing)
        return (x, y)

    # Translate canvas coordinates to (row, col)
    def _xy2rc(self, x, y):
        # how can i optimize it ???? May be _self.canvas.find_withtag(CURRENT)
        for r in range(self._nrows):
            for c in range(self._ncols):
                cell = self._cells[r][c]
                if cell.x < x < cell.x + game2dboard.Cell.width \
                        and cell.y < y < cell.y + game2dboard.Cell.height:
                    return (r, c)
        return None

    # Inner classes
    # ---------------------------------------------------------------

    # A row is a list, so I can use the magic function __setitem__(board[i][j])

    class _BoardRow(UserList):
        # Last acessed row (class member).
        # Yes, its not thread safe!
        # Maybe in the future I will use a proxy class
        current_i = None

        def __init__(self, length, parent):
            UserList.__init__(self)
            self.extend([None] * length)         # Initialize the row
            self._parent = parent           # the board

        def __setitem__(self, j, value):
            self._parent._notify_change(self.__class__.current_i, j, value)
            return super().__setitem__(j, value)
