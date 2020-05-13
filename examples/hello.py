from gui2darray import Board


def kbdfn(key):
    print(key)
    if key == "Escape":                      # http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
        b.close()


b = Board(10, 10)
b.title = "Hello, World!"
b.margin = 7
b.cell_spacing = 1
b.cell_size = (40, 40)
# See color names in http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
b.margin_color = "AntiqueWhite4"
b.cell_color = "AntiqueWhite1"
b.grid_color = "AntiqueWhite4"
b[0][2] = b[4][1] = 160
b.on_key = kbdfn
b.run()
