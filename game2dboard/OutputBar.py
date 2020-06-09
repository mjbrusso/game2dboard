

from tkinter import *
import game2dboard


class OutputBar(Frame):
    def __init__(self, parent, top_margin, **kwargs):
        color=kwargs.get('color')
        background_color=kwargs.get('background_color')
        font_size=kwargs.get('font_size') or 10
        Frame.__init__(self, parent, relief='flat', bg=background_color)
        self.pack(side=BOTTOM, fill=X, expand=True, pady=(top_margin, 0))
        self._label = Label(self, anchor=W,
                            fg=color, bg=background_color,
                            font=(None, font_size))
        self._label.pack(fill=X, expand=True, padx=2, pady=1)

    def show(self, value):
        self._label.configure(text=value)

