from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Mazer Solver") ## Title on the window
        self.canvas = Canvas(self.root, bg="white", height=height, width=width) ## Creates the window
        self.canvas.pack(fill=BOTH, expand=1) ## allows for dynamic resize of the window
        self.window_running = False 
        self.root.protocol("WM_DELETE_WINDOW", self.close) ## ?

    def redraw(self):
        self.root.update()  
        self.root.update_idletasks()      

    def wait_for_close(self):
        self.window_running = True
        while self.window_running == True:
            self.redraw()
    
    def close(self):
        self.window_running = False
    
    def draw_line(self, line, fill_color="red"):
        line.draw(self.canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.y=y
        self.x=x


class Line():
    def __init__(self, st_line, en_line):
        self.st_line = st_line
        self.en_line = en_line

    def draw(self, canvas, fill_color="red"):
        x1, y1 = self.st_line.x, self.st_line.y
        x2, y2 = self.en_line.x, self.en_line.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Cell():
    def __init__(self,w=None,):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._w = w
        self.visited = False
        
    def draw(self, x1, y1, x2, y2):
        if self._w is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1),Point(x1, y2))
            self._w.draw_line(line)
        else:
            line = Line(Point(x1, y1),Point(x1, y2))
            self._w.draw_line(line,"white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._w.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._w.draw_line(line,"white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._w.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._w.draw_line(line,"white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._w.draw_line(line)    
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._w.draw_line(line,"white")


    
    def draw_move(self, to_cell, undo=False):
        self_center_x = (self._x1 + self._x2) // 2
        self_center_y = (self._y1 + self._y2) // 2
        to_cell_center_x = (to_cell._x1 + to_cell._x2) // 2
        to_cell_center_y = (to_cell._y1 + to_cell._y2) // 2

        line_color = "red"
        if undo:
            line_color = "gray"

        line = Line(Point(self_center_x, self_center_y), Point(to_cell_center_x, to_cell_center_y))
        self._w.draw_line(line, fill_color=line_color)

        


        
        

