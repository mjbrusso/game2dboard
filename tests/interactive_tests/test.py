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
[m]   : swap mouse cursor

left click : put/remove monkey 
right click: put fruit
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
    if btn == 1:
        b[row][col] = IMGID if not b[row][col] else None
    elif btn==3:
        b[row][col] = "fruit.png"


def timerfn():
    b.print(datetime.datetime.now().strftime("[H]: Help      %H:%M:%S"))

def startfn():
    b[0][0] = 12
    b[0][1] = "Hello"
    b[0][2] = b[4][1] = IMGID
    b[3][6] = "fruit.png"    

b = Board(5, 15)
b.title = "Hello, World!"
b.margin = 10
b.cell_spacing = 6
b.cell_size = (50, 40)
b.margin_color = b.grid_color = "AntiqueWhite4"
b.cell_color = "AntiqueWhite1"
b.on_start = startfn
b.on_key_press = kbdfn
b.on_mouse_click = mousefn
b.on_timer = timerfn
b.start_timer(1000)
b.create_output(color='gray20', background_color='AntiqueWhite3', font_size=10)
b.show()
