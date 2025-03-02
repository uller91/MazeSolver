from window import Line, Point


class Cell():
    def __init__(self, win, point_1, point_2, l_w = True, r_w = True, t_w = True, b_w = True): #top left and bottom right corners
        self.__x1 = point_1.x
        self.__y1 = point_1.y
        self.__x2 = point_2.x
        self.__y2 = point_2.y
        self.__w = win 
        self.left_wall = l_w
        self.right_wall = r_w
        self.top_wall = t_w
        self.bottom_wall = b_w

    def draw(self, fill_color = "black"):
        if self.left_wall:
            self.__w.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), fill_color)
        if self.right_wall:
            self.__w.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), fill_color)
        if self.top_wall:
            self.__w.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), fill_color)
        if self.bottom_wall:
            self.__w.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), fill_color)

    def draw_move(self, to_cell, undo=False):
        if undo == True:
            fill_color = "grey"
        else:
            fill_color = "red"
        self.__w.draw_line(Line(Point((self.__x1 + self.__x2)/2, (self.__y1 + self.__y2)/2), Point((to_cell.__x1 + to_cell.__x2)/2, (to_cell.__y1 + to_cell.__y2)/2)), fill_color)