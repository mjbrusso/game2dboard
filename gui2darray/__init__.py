__name__ = "gui2darray"
__package__ = "gui2darray"
__version__ = "0.1"

try:
    from tkinter import Tk
except ImportError:
    from Tkinter import Tk

from .Board import Board
from .Cell import Cell
from .ImageMap import ImageMap