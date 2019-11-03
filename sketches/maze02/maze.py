class Grid:
    
    def __init__(self, row, col, gsize):
        self.row = row
        self.col = col
        self.gsize = gsize
        self.walls = {}  # top, left, bottom, right
        self.x = self.gsize*self.col
        self.y = self.gsize*self.row
    
    def connections(self):
        my_list = []
        for key, val in self.walls.items():
            if val != None:
                my_list.append(key)
        return (my_list)
    
    def show(self):
        if self.walls["top"] != None:
            line(self.x, self.y, self.x + self.gsize, self.y)
        if self.walls["left"] != None:
            line(self.x + self.gsize, self.y, self.x + self.gsize, self.y + self.gsize)
        if self.walls["bottom"] != None:
            line(self.x, self.y + self.gsize, self.x + self.gsize, self.y + self.gsize)
        if self.walls["right"] != None:
             line(self.x , self.y, self.x, self.y + self.gsize)

class Maze:
    
    def __init__ (self, nrows, ncols, gsize):
        self.num_rows = nrows
        self.num_cols = ncols
        self.grid_size = gsize
        self.grid = [[Grid(i, j, self.grid_size) for j in range(self.num_cols)] \
                      for i in range(self.num_rows)]
    
    def connect_grid_default(self):
        for grid in self.iter_grid(): # iter_grid ist ein generator
            grid.walls["top"] = self.get_grid(grid.row - 1, grid.col)
            grid.walls["left"] = self.get_grid(grid.row, grid.col + 1)
            grid.walls["bottom"] = self.get_grid(grid.row + 1, grid.col)
            grid.walls["right"] = self.get_grid(grid.row, grid.col - 1)
    
    def get_grid(self, row, col):
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
            return self.grid[row][col]
        else:
            return None
    
    def show(self):
        self.draw_boundary()
        for grid in self.iter_grid():
            grid.show()
    
    def draw_boundary(self):
        # pass
        strokeWeight(5)
        line(0, 0, self.num_cols*self.grid_size, 0)
        line(self.num_rows*self.grid_size, 0, self.num_cols*self.grid_size, self.num_rows*self.grid_size)
        line(self.num_cols*self.grid_size, self.num_rows*self.grid_size, 0, self.num_rows*self.grid_size)
        line(0, self.num_rows*self.grid_size, 0, 0)
        strokeWeight(1)
    
    def iter_grid(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                yield self.grid[i][j]
                
    def print_me(self):
        for grid in self.iter_grid():
            print(grid.row, grid.col, grid.connections())
