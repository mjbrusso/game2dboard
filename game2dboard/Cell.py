from tkinter import *
import game2dboard


# Metaclass for Cell
# Implement static class properties
class CellProperties(type):
    @property
    def width(cls):
        """
        Gets cell width
        """
        return cls.size[0]

    @property
    def height(cls):
        """
        Gets cell height
        """
        return cls.size[1]


class Cell(object, metaclass=CellProperties):
    # (w, h: px) Same size for all cells, so it's a static class member
    size = (50, 50)

    def __init__(self, parent, x, y):
        self._image_id = None       # tkinter id from create_image
        self._value = None          # this value
        self._parent = parent
        self._x = x
        self._y = y
        self._bgcolor = "white"
        self._text_color = "black"
        self._id = parent.create_rectangle(
            x,
            y,
            x+Cell.width,
            y+Cell.height,
            width=0
        )

    @property
    def id(self):
        """
        Gets the rectangle id
        """
        return self._id

    @property
    def value(self):
        """
        Gets or sets the cell value.
        """
        return self._value

    @value.setter
    def value(self, v):
        if self._value != v:        # Only update when value change
            self._value = v
            if self._image_id:
                self._parent.delete(self._image_id)    # clear current image
            if not v is None:
                img = game2dboard.ImageMap.get_instance()[v]
                hc = self._x + Cell.width // 2     # horizontal center
                vc = self._y + Cell.height // 2    # vertical center
                # Show image|text @ canvas center
                if img:
                    self._image_id = self._parent.create_image(  # Draw a image
                        hc,
                        vc,
                        anchor=CENTER,
                        image=img)
                else:
                    self._image_id = self._parent.create_text(  # or just draw the value as text
                        hc,
                        vc,
                        anchor=CENTER,
                        text=str(v),
                        fill=self._text_color,
                        font=(None, max(min(Cell.height//4, 12), 6)),
                        width=Cell.width-2)

    @property
    def bgcolor(self):
        """
        Gets or sets the background color.
        """
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, value):
        self._bgcolor = value
        self._parent.itemconfig(self._id, fill=value)   # Change bg color
        # self._text_color = self._invert_color(value)
        #self._parent.itemconfig(
        #     self._image_id, fill=self._text_color)  # Change text color

    @property
    def x(self):
        """
        Gets x coordinate.
        """
        return self._x

    @property
    def y(self):
        """
        Gets y coordinate.
        """
        return self._y

    # If text color isnt set, create as high contrast color (invert background color)
    # Adapted from https://stackoverflow.com/questions/50327186/how-to-invert-colors-in-tkinters-canvas
    def _invert_color(self, color):
        rgb = self._parent.winfo_rgb(color) if type(color) == str else color
        rgb = (65535-rgb[0], 65535-rgb[1], 65535-rgb[2])
        return "#%04x%04x%04x" % (rgb)
