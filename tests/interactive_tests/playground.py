from game2dboard import Board


b = Board(4, 3)
b.title = "Playground!"
b.margin = 12
b.cell_spacing = 10
b.cell_size = (100, 100)
b.margin_color = "black"
b.grid_color = "red"
b.cell_color = "#303030"
b.background_image = "chess"
b.create_output(color='gray20', background_color='AntiqueWhite3', font_size=10)
b.on_mouse_click = lambda b, r, c : print(r, c)
b.show()
