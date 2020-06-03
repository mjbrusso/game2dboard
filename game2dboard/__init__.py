__name__ = "game2dboard"
__package__ = "game2dboard"
__version__ = "0.7"

try:
    from tkinter import Tk
except ImportError:
    from Tkinter import Tk

from .Board import Board
from .Cell import Cell
from .ImageMap import ImageMap
from .OutputBar import OutputBar

