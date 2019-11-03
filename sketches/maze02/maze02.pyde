from maze import Maze

num_rows = 20
num_cols = 20
grid_size = 32

maze = Maze(num_rows, num_cols, grid_size)

def setup():
    size(650, 650)
    maze.connect_grid_default()
    # maze.print_me()
    noLoop()

def draw():
    background(255, 255, 255)
    stroke(0, 0, 0)
    strokeWeight(1)
    translate(5, 5)
    maze.show()
    
