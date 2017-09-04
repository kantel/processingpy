from random import randint

empty = 0
tree = 1
burning = 20

a = 40
g = 1

nRows = 40
nCols = 40
w = h = 16

grid = []
newgrid = []

def setup():
    global trees, fire
    size(640, 640)
    background(210, 180, 140)
    trees = loadImage("tree.png")
    fire  = loadImage("fire.png")
    for x in range(nRows):
        grid.append([])
        newgrid.append([])
        for y in range(nCols):
            # Randbedingungen
            if (x > 0) and (y > 0) and (x < nRows-1) and (y < nCols-1) and randint(0, 10000) <= 2000:
                grid[x].append(tree)
            else:
                grid[x].append(empty)
    newgrid[:] = grid[:]
    frameRate(2)
    # noLoop()
    
def draw():
    global grid, newgrid
    global trees, fire
    noStroke()
    background(210, 180, 140)
    
    for i in range(nRows):
        for j in range(nCols):
            if grid[i][j] == empty:
                fill(210, 180, 140)
                rect(i*w, j*h, w, h)
            elif grid[i][j] == tree:
                image(trees, i*w, j*h, w, h)
                # fill(255, 0, 0)
                # rect(i*w, j*h, w, h)
            elif grid[i][j] == burning:
                image(fire, i*w, j*h, w, h)
                # fill(0, 255, 0)
                # rect(i*w, j*h, w, h)
    newgrid[:] = grid[:]
    calcNext()
    grid[:] = newgrid[:]
 
def calcNext():
    global grid, newgrid
    # Next Generation
    for i in range(1, nRows-1):
        for j in range(1, nCols-1):
            if grid[i][j] == burning:
                newgrid[i][j] = empty
            elif grid[i][j] == empty:
                if randint(0, 10000) < a:
                    newgrid[i][j] = tree
            elif grid[i][j] == tree:
            # Schlägt ein Blitz ein?
                if (random(10000) < 1):
                    newgrid[i][j] = burning
            # Brennt ein Nachbar?
                elif(grid[i-1][j] + grid[i][j-1] + grid[i][j + 1] + grid[i+1][j] >= burning):
                    newgrid[i][j] = burning