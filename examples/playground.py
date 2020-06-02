from gui2darray import Board


def fnm(btn, r, c):
    if btn==1 or btn==4:
        b[r][c] += 1
    else:
        b[r][c] -= 1

b = Board(4, 4)
b.fill(0)
b[1][0] = 3
b[1][1] = 40
# b.cell_color = "green"
# b.grid_color = "white"
b.on_mouse_click = fnm
b.show()
