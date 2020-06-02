from game2dboard import Board
from tkinter import messagebox
import datetime

IMGID = 160

def kbdfn(key):
    b.print("You pressed [{}] key".format(key))   # http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
    if key == "Escape" and messagebox.askyesno(b.title, "Deseja mesmo sair do programa?"):  # https://www.tutorialspoint.com/python3/tk_messagebox.htm
        b.close()
    elif key == "h":
        messagebox.showinfo("Help", """
[ESC] : close
[h]   : help
[r]   : shuffle 
[f]   : fill all board
[1]   : fill collumn[1]
[2]   : fill row[2]
[c]   : clear
[t]   : start/stop timer
[m]   : swap mouse cursor

click : put/remove
        """)
    elif key == "r":
        b.shuffle()
    elif key == "f":
        b.fill(IMGID)
    elif key == "c":
        b.clear()
    elif key == "1":
        b.fill(IMGID, col=1)
    elif key == "2":
        b.fill(IMGID, row=2)
    elif key == "m":
        b.cursor = "arrow" if b.cursor == "hand1" else "hand1"

def mousefn(btn, row, col):
    b.print("You clicked button {} on b[{}][{}]".format(btn, row, col))
    b[row][col] = IMGID if not b[row][col] else None

def timerfn():
    b.print(datetime.datetime.now().strftime("[H]: Help      %H:%M:%S"))

b = Board(5, 15)
b[0][0] = 12
b.title = "Hello, World!"
# See available cursor names in https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
#b.cursor = "hand1"
b.margin = 7
b.cell_spacing = 1
b.cell_size = (50, 40)
# See color names in http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
b.margin_color = b.grid_color = "AntiqueWhite4"
b.cell_color = "AntiqueWhite1"
b[0][2] = b[4][1] = IMGID
b.on_key_press = kbdfn
b.on_mouse_click = mousefn
b.on_timer = timerfn
b.start_timer(1000)
b.create_output(color='gray20', background_color='AntiqueWhite3', font_size=10)
b.show()
