from gui2darray import Board


def kbdfn(key):
    print(key)
    if key == "Escape":                      # http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
        b.close()    
    elif key == "space":
        b[3][3] = 160 if not b[3][3] else None
    elif key == "r":
        b.shuffle()
    elif key == "a":
        b.fill(160)
    elif key == "c":
        b.fill(None)
    elif key == "1":
        b.fill(160, col=1)
    elif key == "2":
        b.fill(160, row=2)
    elif key == "x":
        b.fill(None, col=1, row=1)

b = Board(10, 10)
b.title = "Hello, World!"
b.margin = 7
b.cell_spacing = 1
#b.cell_size = (40, 40)
# See color names in http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
b.margin_color = "AntiqueWhite4"
b.cell_color = "AntiqueWhite1"
b.grid_color = "AntiqueWhite4"
b[0][2] = b[4][1] = 160
b.on_key_press = kbdfn
b.run()
