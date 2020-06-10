from game2dboard import *


caught = total = 0

def timer_fn():
    global caught, total
    b.clear()
    b[0][0] = "mosquito"
    b.shuffle()
    total += 1
    b.print(caught, "/", total)


def mouse_fn(button, row, col):
    global caught
    if b[row][col] == "mosquito":
        caught += 1
        b.print(caught, "/", total)
        b[row][col] = "injured"


b = Board(10, 10)
b.title = "Tap the mosquito"
b.cursor = "draped_box"
b.cell_size = (50, 50)
b.cell_color = "black"
b.cell_spacing = 1
b.grid_color = b.margin_color = "gray5"
b.create_output(background_color="gray10", color="white")
b.on_mouse_click = mouse_fn
b.on_timer = timer_fn
b.start_timer(800)
b.show()
