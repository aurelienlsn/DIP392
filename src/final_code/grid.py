class Grid:
    def __init__(self, rows, columns):
        if rows <= 0 or columns <= 0:
            raise ValueError("Grid size must be positive")
        self.gridSize = (rows, columns)
        self.gridLayout = [[None for _ in range(columns)] for _ in range(rows)]

    def displayGrid(self):
        for row in self.gridLayout:
            print(' '.join(['O' if disc is None else disc.discColor for disc in row]))
