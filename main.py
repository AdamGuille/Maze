from windowing import Window, Line, Point

def main():
    win = Window(800, 600)
    l = (Line(Point(85, 30), Point(400, 400)))
    win.draw_line(l, "green")
    win.wait_for_close()

main()