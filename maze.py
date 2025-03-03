import time

from tkinter import Tk, BOTH, Canvas
from window import Point
from cell import Cell

class Maze():
    def __init__(self, win, corner, num_columns, num_rows, cell_size_x, cell_size_y):
        self._w = win
        self._x = corner.x
        self._y = corner.y
        self._num_columns = num_columns
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []

        self.__create_cells()

    def __create_cells(self):
        for i in range(self._num_columns):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._w, Point(self._x + i * self._cell_size_x, self._y + j * self._cell_size_y), Point(self._x + (i + 1) * self._cell_size_x, self._y + (j + 1) * self._cell_size_y)))
            self._cells.append(column)
        #print(self.__cells)

        self.__draw_cell()

    def __draw_cell(self):
        for column in self._cells:
            for cell in column:
                cell.draw()
                self.__animate()

    def __animate(self):
        self._w.redraw()
        time.sleep(0.05)

    #def __break_entrance_and_exit(self):
