

from tkinter import Label
import gui2darray

class MessageBar(Label):
    def __init__(self, parent, w):
        self.parent = parent
        Tkinter.Text.__init__(self, self.Frame, width=w, height=1)
        # .message_bar {.height, .bgcolor, font_size, .font_color, .text }  
