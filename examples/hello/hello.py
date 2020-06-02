from gui2darray import Board

def fntimer():
    b.shuffle()
    b.start_timer(500)

b = Board(3, 12)
b[1][0] = 'H'
b[1][1] = 'e'
b[1][2] = 'l'
b[1][3] = 'l'
b[1][4] = 'o'
b[1][5] = 'comma'
b[1][6] = 'W'
b[1][7] = 'o'
b[1][8] = 'r'
b[1][9] = 'l'
b[1][10] = 'd'
b[1][11] = 'excl'

b.cell_size = (80, 100)
b.title = "WTF????"
b.margin = 10
b.cell_spacing = 3
b.grid_color = b.margin_color = "AntiqueWhite3"
b.cell_color = "gray20"
b.start_timer(2000)
b.on_timer = fntimer
b.show()

