from gui2darray import Board

b = Board(70, 70)
b.title = "Hello, World!"
b.margin = 5
b.cell_spacing = 2
b.cell_size = (15, 8)
b.margin_color = "AntiqueWhite3"      # See color names in http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
b.cell_color = "AntiqueWhite1"
b.grid_color = "AntiqueWhite3"

b.run()
