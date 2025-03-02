import time

from tkinter import Tk, BOTH, Canvas
from window import Point
from cell import Cell

class Maze():
    def __init__(self, win, corner, num_columns, num_rows, cell_size_x, cell_size_y):
        self.__w = win
        self.__x = corner.x
        self.__y = corner.y
        self.__num_columns = num_columns
        self.__num_rows = num_rows
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__cells = []

        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_columns):
            column = []
            for j in range(self.__num_rows):
                column.append(Cell(self.__w, Point(self.__x + i * self.__cell_size_x, self.__y + j * self.__cell_size_y), Point(self.__x + (i + 1) * self.__cell_size_x, self.__y + (j + 1) * self.__cell_size_y)))
            self.__cells.append(column)
        #print(self.__cells)

        self.__draw_cell()

    def __draw_cell(self):
        for column in self.__cells:
            for cell in column:
                cell.draw()
                self.__animate()

    def __animate(self):
        self.__w.redraw()
        time.sleep(0.05)