from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height, title = "Maze Solver"):
        self.__root = Tk()
        self.__root.title(title)
        #self.__width = width
        #self.__height = height
        self.__canvas = Canvas(self.__root, bg="green", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Maze solver closed.")

    def close(self):
        self.__is_running = False