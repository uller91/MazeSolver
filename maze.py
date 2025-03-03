import time
import random

from tkinter import Tk, BOTH, Canvas
from window import Point
from cell import Cell

class Maze():
    def __init__(self, corner, num_columns, num_rows, cell_size_x, cell_size_y, win = None, seed = None):
        self._w = win
        self._x = corner.x
        self._y = corner.y
        self._num_columns = num_columns
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._seed = seed
        
        random.seed(self._seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_v0_r(0,0)

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

    def _break_walls_v0_r(self, i, j):
        
        if i == self._num_columns:
            self._reset_cells_visited()
            #print("last cell")
            return

        self._cells[i][j].visited = True
        neighbours = []
        #print(f"{i} and {j}")
        if i != 0:
            neighbours.append([i-1, j])
        if i != self._num_columns-1:
            neighbours.append([i+1, j])
        if j != 0:
            neighbours.append([i, j-1])
        if j != self._num_rows-1:
            neighbours.append([i, j+1])
        #print(neighbours)
        
        walls = ["left", "right", "top", "bottom"]
        walls_to_break = random.sample(walls, random.randint(1, 2))

        for wall in walls_to_break:
            match wall:
                case "left":
                    self._cells[i][j].left_wall = False
                    if [i-1, j] in neighbours:
                        self._cells[i-1][j].right_wall = False
                        self._draw_cell(i-1, j)
                case "right":
                    self._cells[i][j].right_wall = False
                    if [i+1, j] in neighbours:
                        self._cells[i+1][j].left_wall = False
                        self._draw_cell(i+1, j)
                case "top":
                    self._cells[i][j].top_wall = False
                    if [i, j-1] in neighbours:
                        self._cells[i][j-1].bottom_wall = False
                        self._draw_cell(i, j-1)
                case "bottom":
                    self._cells[i][j].bottom_wall = False
                    if [i, j+1] in neighbours:
                        self._cells[i][j+1].top_wall = False
                        self._draw_cell(i, j+1)
    
        if j == self._num_rows-1:
            self._break_walls_v0_r(i+1, 0)
        else:
            self._break_walls_v0_r(i, j+1)

    def _reset_cells_visited(self):
        for i in range(self._num_columns):
                for j in range(self._num_rows):
                    self._cells[i][j].visited = False

    def solve(self, i, j):
        return self._solve_r(i, j)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_columns-1 and j == self._num_rows-1:
            return True

        available_neighbours = []
        #print(f"{i} and {j}")
        if i != 0 and self._cells[i][j].left_wall == False and self._cells[i-1][j].visited == False:
            available_neighbours.append([i-1, j])
        if i != self._num_columns-1 and self._cells[i][j].right_wall == False and self._cells[i+1][j].visited == False:
            available_neighbours.append([i+1, j])
        if j != 0 and self._cells[i][j].top_wall == False and self._cells[i][j-1].visited == False:
            available_neighbours.append([i, j-1])
        if j != self._num_rows-1 and self._cells[i][j].bottom_wall == False and self._cells[i][j+1].visited == False:
            available_neighbours.append([i, j+1])
        for neighbour in available_neighbours:
            i_n = neighbour[0]
            j_n = neighbour[1]
            self._cells[i][j].draw_move(self._cells[i_n][j_n])
            if self._solve_r(i_n, j_n):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i_n][j_n], True)

        return False



"""
dfs
    def depth_first_search(self, start_vertex):    
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        sorted_neighbors = sorted(self.graph[current_vertex])
        for neighbor in sorted_neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)
"""