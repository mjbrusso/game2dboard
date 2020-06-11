from game2dboard import Board


b = Board(8, 8)
b.title = "Playground!"
b.margin = 0
b.cell_spacing = 1
b.cell_size = 80
b.margin_color = None
b.grid_color = "red"
b.cell_color = "green"
b.create_output(color='gray20', background_color='AntiqueWhite3', font_size=10)
b.show()
