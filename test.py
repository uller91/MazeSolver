import unittest

from maze import Maze
from window import Window, Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0,0), num_cols, num_rows, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 10
        num_rows = 12
        m2 = Maze(Point(0,0), num_cols, num_rows, 10, 10)

        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_zero_cols(self): #[]
        num_cols = 0
        num_rows = 12
        m3 = Maze(Point(0,0), num_cols, num_rows, 10, 10)

        self.assertEqual(
            m3._cells,
            [],
        )

    def test_maze_create_cells_zero_rows(self): #12 elements of []
        num_cols = 12
        num_rows = 0
        m4 = Maze(Point(0,0), num_cols, num_rows, 10, 10)

        self.assertEqual(
            len(m4._cells),
            num_cols,
        )
        self.assertEqual(
            m4._cells[0],
            [],
        )

    def test_maze_entrance_and_exit(self): #12 elements of []
        num_cols = 6
        num_rows = 6
        m5 = Maze(Point(0,0), num_cols, num_rows, 10, 10)
        m5._break_entrance_and_exit()

        self.assertEqual(
            m5._cells[0][0].left_wall,
            False,
        )
        self.assertEqual(
            m5._cells[num_cols-1][num_rows-1].right_wall,
            False,
        )


if __name__ == "__main__":
    unittest.main()