import time

from window import Window, Point
from cell import Cell
from maze import Maze
            

def main():
    #print("Hello world!")

    #window created
    win = Window(800, 600)

    #drawing
    maze = Maze(Point(100, 100), 12, 8, 50, 50, win, 0) # seed = 0 - a good seed
    maze.solve(0, 0)

    #waiting for the window to close
    win.wait_for_close()


main()