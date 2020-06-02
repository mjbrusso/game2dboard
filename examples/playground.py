from game2dboard import Board


def mouse_fn(btn, row, col):
    if btn==1 or btn==4:
        b[row][col] += 1
    else:
        b[row][col] -= 1

b = Board(4, 4)
b.cell_size = 100
b.fill(0)
b.cell_color = "white"
b.grid_color = "black"
b[1][0] = 10
b.on_mouse_click = mouse_fn
b.create_output()
b.print("<left-button>: Increment    <right button>: Decrement")
b.show()
