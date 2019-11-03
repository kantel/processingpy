from maze import Maze

num_rows = 20
num_cols = 20
grid_size = 32

maze = Maze(num_rows, num_cols, grid_size)

def setup():
    size(640, 640)
    maze.connect_grid_default()
    maze.print_me()
