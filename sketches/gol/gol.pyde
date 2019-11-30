from copy import deepcopy

resolution = 10
grid = []
next = []

def setup():
    global grid, next, cols, rows
    size(600, 400)
    this.surface.setTitle("Conways Game of Life")
    cols = width / resolution
    rows = height / resolution
    
    grid = [[floor(random(2)) for _ in range(rows)] for _ in range(cols)]
    next = [[0 for _ in range(rows)] for _ in range(cols)]
    frameRate(30)

def draw():
    global grid, next, cols, rows
    background(255)
    for i in range(cols):
        for j in range(rows):
            x = i * resolution
            y = j * resolution
            if grid[i][j] == 1:
                fill(255, 0, 0)
                stroke(0)
                rect(x, y, resolution, resolution)
            else:
                fill(200)
                stroke(0)
                rect(x, y, resolution, resolution)
    
    # Nächste Generation
    for i in range(cols):
        for j in range(rows):
            state = grid[i][j]
            neighbors = count_neighbors(grid, i, j)
            if ((state == 0) and (neighbors == 3)):
                next[i][j] = 1
            elif ((state == 1) and (neighbors < 2 or neighbors > 3)):
                next[i][j] = 0
            else:
                next[i][j] = state
    
    grid = deepcopy(next)
            
    
def count_neighbors(li, x, y):
    global cols, rows
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (x + i + cols) % cols
            row = (y + j + rows) % rows
            sum += li[col][row]
    sum -= li[x][y]
    return(sum)
