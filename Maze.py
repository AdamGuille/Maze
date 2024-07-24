from windowing import Cell
import time


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.win = win

        self._create_cells()
        
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
            self._cells.append(column)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self._cell_size_y 
        x2 = x1 + self.cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[j][i].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)