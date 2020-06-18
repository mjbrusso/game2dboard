from game2dboard import Board


b = Board(2, 2)
b[0][0] = 5
b[1][1] = 10
print(b)
a = b.copy()
print(a)
b.title = "Hi!"
b.grid_color = None
b.on_mouse_click = lambda b, r, c: print(type(b), type(r), type(c))
b.show()
