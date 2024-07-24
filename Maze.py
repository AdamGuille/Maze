from windowing import Cell

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.win = win
        
    def _create_cells(self):
        self._cells = []
        for c in range(self.num_cols):
            column = []
            for r in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
                self._draw_cell(r,c)
            self._cells.append(column)

    def _draw_cell(self, i, j):
        
        pass