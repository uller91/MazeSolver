import time

from tkinter import Tk, BOTH, Canvas
from window import Point
from cell import Cell

class Maze():
    def __init__(self, corner, num_columns, num_rows, cell_size_x, cell_size_y, win = None):
        self._w = win
        self._x = corner.x
        self._y = corner.y
        self._num_columns = num_columns
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_columns):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._w, Point(self._x + i * self._cell_size_x, self._y + j * self._cell_size_y), Point(self._x + (i + 1) * self._cell_size_x, self._y + (j + 1) * self._cell_size_y)))
            self._cells.append(column)

        for i in range(self._num_columns):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._w is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._w is None:
            return
        self._w.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].left_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_columns-1][self._num_rows-1].right_wall = False
        self._draw_cell(self._num_columns-1, self._num_rows-1)
