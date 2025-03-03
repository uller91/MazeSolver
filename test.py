import unittest

from maze import Maze
from window import Window, Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(win, Point(0,0), num_cols, num_rows, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        win = Window(800, 600)
        num_cols = 10
        num_rows = 12
        m1 = Maze(win, Point(0,0), num_cols, num_rows, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_zero_cols(self): #[]
        win = Window(800, 600)
        num_cols = 0
        num_rows = 12
        m1 = Maze(win, Point(0,0), num_cols, num_rows, 10, 10)

        self.assertEqual(
            m1._cells,
            [],
        )

    def test_maze_create_cells_zero_rows(self): #12 elements of []
        win = Window(800, 600)
        num_cols = 12
        num_rows = 0
        m1 = Maze(win, Point(0,0), num_cols, num_rows, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            m1._cells[0],
            [],
        )


if __name__ == "__main__":
    unittest.main()