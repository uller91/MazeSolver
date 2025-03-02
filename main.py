from window import Window, Line, Point
from cell import Cell
            

def main():
    #print("Hello world!")

    #window created
    win = Window(800, 600)

    #drawing
    #win.draw_line(Line(Point(100, 100), Point(300, 300)), "black")
    #win.draw_line(Line(Point(100, 300), Point(300, 100)), "black")
    cell_1 = Cell(win, Point(100, 100), Point(300, 300))
    cell_1.draw()

    cell_2 = Cell(win, Point(300, 100), Point(500, 300))
    cell_2.draw()

    cell_3 = Cell(win, Point(300, 300), Point(500, 500), l_w = False, b_w = False)
    cell_3.draw("white")

    cell_4 = Cell(win, Point(300, 300), Point(500, 500), r_w = False, t_w = False)
    cell_4.draw("red")

    cell_5 = Cell(win, Point(500, 100), Point(700, 300), r_w = False, t_w = False, b_w = False)
    cell_5.draw("blue")

    cell_6 = Cell(win, Point(500, 100), Point(700, 300), l_w = False, t_w = False, b_w = False)
    cell_6.draw("blue")

    cell_7 = Cell(win, Point(500, 100), Point(700, 300), r_w = False, l_w = False, b_w = False)
    cell_7.draw("yellow")\
    
    cell_8 = Cell(win, Point(500, 100), Point(700, 300), l_w = False, t_w = False, r_w = False)
    cell_8.draw("yellow")


    #waiting for the window to close
    win.wait_for_close()


main()