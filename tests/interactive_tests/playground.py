from game2dboard import Board


b = Board(4, 4)
b.title = "oi"
b.on_mouse_click = lambda b, r, c: print(type(b), type(r), type(c))
b.show()
