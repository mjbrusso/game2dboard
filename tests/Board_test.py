from tkinter import *
from game2dboard import Board

all_tests = []


def add_test(f): all_tests.append(f)


TIME_TO_CLOSE = 100

def size_test():
    b = Board(3, 5)
    assert b.nrows == 3
    assert b.ncols == 5
    assert b.size == 15
    b._setupUI()
    assert b.nrows == 3
    assert b.ncols == 5
    assert b.size == 15


add_test(size_test)


def title_test():
    b = Board(2, 2)
    _value = "qwertyu 213213  dsdadasd~...."
    b.title = _value
    assert b.title == _value
    b._setupUI()
    assert b.title == _value
    assert b._root.title() == _value
    b.on_timer = lambda: b.close()
    b.start_timer(TIME_TO_CLOSE)
    b.show()
    assert b.title == _value
    assert b._root.title() == _value    


add_test(title_test)


def cursor_test():
    b = Board(1, 20)
    _value = "watch"
    b.cursor = _value
    assert b.cursor == _value
    b._setupUI()
    assert b.cursor == _value
    b.on_timer = lambda: b.close()
    b.start_timer(TIME_TO_CLOSE)
    b.show()
    assert b.cursor == _value

add_test(cursor_test)


def margin_test():
    b = Board(7, 1)
    _value = 19
    b.margin = _value
    assert b.margin == _value
    b._setupUI()
    assert b.margin == _value
    b.on_timer = lambda: b.close()
    b.start_timer(TIME_TO_CLOSE)
    b.show()
    assert b.margin == _value    


add_test(margin_test)


def cell_spacing_test():
    b = Board(1, 1)
    _value = 7
    b.cell_spacing = _value
    assert b.cell_spacing == _value
    b._setupUI()
    assert b.cell_spacing == _value
    b.on_timer = lambda: b.close()
    b.start_timer(TIME_TO_CLOSE)
    b.show()
    assert b.cell_spacing == _value    


add_test(cell_spacing_test)


def margin_color_test():
    b = Board(10, 10)
    _value = "dark gray"
    b.margin_color = _value
    assert b.margin_color == _value
    b._setupUI()
    assert b.margin_color == _value
    b.on_timer = lambda: b.close()
    b.start_timer(TIME_TO_CLOSE)
    b.show()
    assert b.margin_color == _value    


add_test(margin_color_test)


def cell_color_test():
    b = Board(4, 9)
    _value = "#000fff000"
    b.cell_color = _value
    assert b.cell_color == _value
    b._setupUI()
    assert b.cell_color == _value
    b.on_timer = lambda: b.close()
    b.start_timer(TIME_TO_CLOSE)
    b.show()
    assert b.cell_color == _value    


add_test(cell_color_test)


def grid_color_test():
    b = Board(4, 9)
    _value = "magenta"
    b.grid_color = _value
    assert b.grid_color == _value
    b._setupUI()
    assert b.grid_color == _value
    b.on_timer = lambda: b.close()
    b.start_timer(TIME_TO_CLOSE)
    b.show()
    assert b.grid_color == _value    


add_test(grid_color_test)


def cell_size_test():
    b = Board(4, 9)
    _value  = (34, 55)
    b.cell_size = _value
    assert b.cell_size[0] == _value[0]
    assert b.cell_size[1] == _value[1]
    b._setupUI()
    assert b.cell_size[0] == _value[0]
    assert b.cell_size[1] == _value[1]
    b.on_timer = lambda: b.close()
    b.start_timer(TIME_TO_CLOSE)
    b.show()
    assert b.cell_size[0] == _value[0]
    assert b.cell_size[1] == _value[1]


    b2 = Board(42, 99)
    _value  = 1
    b2.cell_size = _value
    assert b2.cell_size[0] == _value
    assert b2.cell_size[1] == _value
    b2._setupUI()
    assert b2.cell_size[0] == _value
    assert b2.cell_size[1] == _value
    b2.on_timer = lambda: b.close()
    b2.start_timer(TIME_TO_CLOSE)
    b2.show()
    assert b2.cell_size[0] == _value
    assert b2.cell_size[1] == _value    


add_test(cell_size_test)


if __name__ == "__main__":
    for fn in all_tests:
        fn()

    print("Everything ok!")
