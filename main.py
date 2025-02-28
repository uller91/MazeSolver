from window import *
            

def main():
    #print("Hello world!")

    #window created
    win = Window(800, 600)

    #drawing
    win.draw_line(Line(Point(100, 100), Point(300, 300)), "black")
    win.draw_line(Line(Point(100, 300), Point(300, 100)), "black")

    #waiting for the window to close
    win.wait_for_close()


main()