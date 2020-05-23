from gui2darray import Board

def fntimer():
    b.shuffle()
    b.timer_interval = 500

b = Board(3, 12)
b[0][0] = 'H'
b[0][1] = 'e'
b[0][2] = 'l'
b[0][3] = 'l'
b[0][4] = 'o'
b[0][5] = 'comma'
b[0][6] = 'W'
b[0][7] = 'o'
b[0][8] = 'r'
b[0][9] = 'l'
b[0][10] = 'd'
b[0][11] = 'excl'

b.cell_size = (80, 100)
b.title = "WTF????"
b.margin = 10
b.cell_spacing = 3
b.grid_color = b.margin_color = "AntiqueWhite3"
b.cell_color = "gray20"
b.timer_interval = 2000
b.on_timer = fntimer
b.show()

