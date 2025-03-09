import time

from window import Window, Point
from cell import Cell
from maze import Maze
            

def main():
    #window created
    win = Window(800, 600)

    #drawing
    maze = Maze(Point(100, 100), 12, 8, 50, 50, win) # seed = 0 - a good seed
    
    #solving the maze
    result = maze.solve(0, 0)
    if result == True:
        print("The mase is solved!")
    else:
        print("The soluition for this maze doesn't exist!")


    #waiting for the window to close
    win.wait_for_close()


main()