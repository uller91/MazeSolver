from window import Line, Point


class Cell():
    def __init__(self, win, point_1, point_2, l_w = True, r_w = True, t_w = True, b_w = True): #top left and bottom right corners
        self._x1 = point_1.x
        self._y1 = point_1.y
        self._x2 = point_2.x
        self._y2 = point_2.y
        self._w = win 
        self.left_wall = l_w
        self.right_wall = r_w
        self.top_wall = t_w
        self.bottom_wall = b_w

    def draw(self, fill_color = "black"):
        if self.left_wall:
            self._w.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_color)
        else:
            self._w.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "green")

        if self.right_wall:
            self._w.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill_color)
        else:
            self._w.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "green")

        if self.top_wall:
            self._w.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_color)
        else:
            self._w.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "green")

        if self.bottom_wall:
            self._w.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_color)
        else:
            self._w.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "green")

    def draw_move(self, to_cell, undo=False):
        if undo == True:
            fill_color = "grey"
        else:
            fill_color = "red"
        self._w.draw_line(Line(Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2), Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)), fill_color)