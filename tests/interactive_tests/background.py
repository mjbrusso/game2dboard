from game2dboard import Board

b = Board(8, 8)
b.title = "Playground!"
b.margin = 21
b.cell_size = 74
b.cell_spacing = 1
b.background_image = "chess"
b.create_output(color='gray20', background_color='AntiqueWhite3', font_size=10)
b.on_mouse_click = lambda btn, r, c : b.print("Clicked on [{}][{}]".format(r, c))
b.print("Click me")
b.show()