from gui2darray import Board

b = Board(3, 3)
b.title = "Hello, World!"

b.margin = 10
b.cell_spacing = 3
b.cell_size = (100, 100)
b.margin_color = "AntiqueWhite3"      # See color names in http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
b.cell_color = "AntiqueWhite1"
b.grid_color = "AntiqueWhite3"

b.run()
