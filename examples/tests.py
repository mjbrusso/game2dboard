from gui2darray import Board

import datetime

def kbdfn(key):
    b.print("You pressed [{}] key".format(key))
    if key == "Escape":                      # http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
        b.close()
    elif key == "r":
        b.shuffle()
    elif key == "a":
        b.fill(160)
    elif key == "c":
        b.clear()
    elif key == "1":
        b.fill(160, col=1)
    elif key == "2":
        b.fill(160, row=2)
    elif key == "t":
        b.timer_interval = 0 if b.timer_interval else 1000
    elif key == "m":
        b.cursor = "arrow" if b.cursor == "hand1" else "hand1"

def mousefn(btn, row, col):
    b.print("You clicked button {} on b[{}][{}]".format(btn, row, col))
    b[row][col] = 160 if not b[row][col] else None

def timerfn():
    b.print(datetime.datetime.now().strftime("%H:%M:%S"))

b = Board(5, 15)
b.title = "Hello, World!"
# See available cursor names in https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
#b.cursor = "hand1"
b.margin = 7
b.cell_spacing = 1
b.cell_size = (50, 40)
# See color names in http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
b.margin_color = b.grid_color = "AntiqueWhite4"
b.cell_color = "AntiqueWhite1"
b[0][2] = b[4][1] = 160
b.on_key_press = kbdfn
b.timer_interval = 1000
b.on_mouse_click = mousefn
b.on_timer = timerfn
b.create_output(color='gray20', background_color='AntiqueWhite3', font_size=10)
b.run()
