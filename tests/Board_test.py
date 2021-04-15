from tkinter import *
from game2dboard import Board
import unittest


TIME_TO_CLOSE = 100


class TestBoard(unittest.TestCase):
    def test_size(self):
        b = Board(3, 5)
        self.assertEqual(b.nrows, 3)
        self.assertEqual(b.ncols, 5)
        self.assertEqual(b.size, 15)
        b._setupUI()
        self.assertEqual(b.nrows, 3)
        self.assertEqual(b.ncols, 5)
        self.assertEqual(b.size, 15)

    def test_title(self):
        b = Board(2, 2)
        _value = "qwertyu 213213  dsdadasd~...."
        b.title = _value
        self.assertEqual(b.title, _value)
        b._setupUI()
        self.assertEqual(b.title, _value)
        self.assertEqual(b._root.title(), _value)
        b.on_timer = lambda: b.close()
        b.start_timer(TIME_TO_CLOSE)
        b.show()
        self.assertEqual(b.title, _value)
        self.assertEqual(b._root.title(), _value)

    def test_cursor(self):
        b = Board(1, 20)
        _value = "watch"
        b.cursor = _value
        self.assertEqual(b.cursor, _value)
        b._setupUI()
        self.assertEqual(b.cursor, _value)
        b.on_timer = lambda: b.close()
        b.start_timer(TIME_TO_CLOSE)
        b.show()
        self.assertEqual(b.cursor, _value)

    def test_margin(self):
        b = Board(7, 1)
        _value = 19
        b.margin = _value
        self.assertEqual(b.margin, _value)
        b._setupUI()
        self.assertEqual(b.margin, _value)
        b.on_timer = lambda: b.close()
        b.start_timer(TIME_TO_CLOSE)
        b.show()
        self.assertEqual(b.margin, _value)

    def test_cell_spacing(self):
        b = Board(1, 1)
        _value = 7
        b.cell_spacing = _value
        self.assertEqual(b.cell_spacing, _value)
        b._setupUI()
        self.assertEqual(b.cell_spacing, _value)
        b.on_timer = lambda: b.close()
        b.start_timer(TIME_TO_CLOSE)
        b.show()
        self.assertEqual(b.cell_spacing, _value)

    def test_margin_color(self):
        b = Board(10, 10)
        _value = "dark gray"
        b.margin_color = _value
        self.assertEqual(b.margin_color, _value)
        b._setupUI()
        self.assertEqual(b.margin_color, _value)
        b.on_timer = lambda: b.close()
        b.start_timer(TIME_TO_CLOSE)
        b.show()
        self.assertEqual(b.margin_color, _value)

    def test_cell_color(self):
        b = Board(4, 9)
        _value = "#000fff000"
        b.cell_color = _value
        self.assertEqual(b.cell_color, _value)
        b._setupUI()
        self.assertEqual(b.cell_color, _value)
        b.on_timer = lambda: b.close()
        b.start_timer(TIME_TO_CLOSE)
        b.show()
        self.assertEqual(b.cell_color, _value)

    def test_grid_color(self):
        b = Board(4, 9)
        _value = "magenta"
        b.grid_color = _value
        self.assertEqual(b.grid_color, _value)
        b._setupUI()
        self.assertEqual(b.grid_color, _value)
        b.on_timer = lambda: b.close()
        b.start_timer(TIME_TO_CLOSE)
        b.show()
        self.assertEqual(b.grid_color, _value)

    def test_cell_size(self):
        b = Board(4, 9)
        _value = (34, 55)
        b.cell_size = _value
        self.assertEqual(b.cell_size[0], _value[0])
        self.assertEqual(b.cell_size[1], _value[1])
        b._setupUI()
        self.assertEqual(b.cell_size[0], _value[0])
        self.assertEqual(b.cell_size[1], _value[1])
        b.on_timer = lambda: b.close()
        b.start_timer(TIME_TO_CLOSE)
        b.show()
        self.assertEqual(b.cell_size[0], _value[0])
        self.assertEqual(b.cell_size[1], _value[1])

        b2 = Board(42, 99)
        _value = 1
        b2.cell_size = _value
        self.assertEqual(b2.cell_size[0], _value)
        self.assertEqual(b2.cell_size[1], _value)
        b2._setupUI()
        self.assertEqual(b2.cell_size[0], _value)
        self.assertEqual(b2.cell_size[1], _value)
        b2.on_timer = lambda: b.close()
        b2.start_timer(TIME_TO_CLOSE)
        b2.show()
        self.assertEqual(b2.cell_size[0], _value)
        self.assertEqual(b2.cell_size[1], _value)

    def test_fill(self):
        b = Board(3, 3)
        b.fill('ZZZ', row=1)
        self.assertEqual(b[1].count('ZZZ'), 3)
        b.fill(1.5, col=2)
        self.assertEqual(b[0][2], 1.5)
        self.assertEqual(b[1][2], 1.5)
        self.assertEqual(b[2][2], 1.5)
        b.fill(-3)
        for i in range(b.nrows):        
            self.assertTrue(all(v==-3 for v in b[i]))


    def test_copy(self):
        b = Board(2, 3)
        for i in range(b.nrows):
            for j in range(b.ncols):
                b[i][j] = (i+1) * (j+5)

        bc = b.copy()
        self.assertEqual(len(bc), b.nrows)        
        for i in range(len(bc)):
            self.assertEqual(len(bc[i]), b.ncols)
            for j in range(len(bc[i])):
                self.assertEqual(bc[i][j], b[i][j])

    def test_load(self):
        b = Board(2, 2)
        b.load([[10, 20], ['a', False]])
        self.assertEqual(b[0][0], 10)
        self.assertEqual(b[0][1], 20)
        self.assertEqual(b[1][0], 'a')
        self.assertEqual(b[1][1], False)


if __name__ == "__main__":
    unittest.main()
