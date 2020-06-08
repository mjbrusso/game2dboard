from game2dboard import Board


def mouse_fn(btn, row, col):    # mouse calback function
    b[row][col] = 1 if not b[row][col] else 0    

b = Board(3, 2)         # 3 rows, 4 columns, filled w/ None
b[0][0] = 100
b.title = "Click me!"
b.cell_size = 50       
b.cell_color = "bisque"
b.on_mouse_click = mouse_fn
b.show()
