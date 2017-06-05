import random as r

empty = 0
frog = 1
turtle = 2

nRows = 40
nCols = 40
w = h = 16

jumpsize = 2

def setup():
    global grid, frogs, turts, lilys
    size(640, 640)
    noStroke()
    background(0)
    frogs = loadImage("frog.png")
    turts = loadImage("turtle.png")
    lilys = loadImage("lily.png")
    grid = []
    for x in xrange(nRows):
        grid.append([])
        for y in xrange(nCols):
            grid[x].append(r.randint(0, 2))
            if grid[x][y] == empty:
                image(lilys, x*w, y*h, w, h)
            elif grid[x][y] == frog:
                image(frogs, x*w, y*h, w, h)
            elif grid[x][y] == turtle:
                image(turts, x*w, y*h, w, h)
            else:
                println("Etwas ist falsch im Staate Lilypond!")
            

def draw():
    global grid, frogs, turts, lilys
    noStroke()
    background(0)
    
    actorX = r.randint(0, nRows-2)
    actorY = r.randint(0, nCols-2)
    if grid[actorX][actorY] > 0:
        happy = isHappy(grid[actorX][actorY], actorX, actorY)
        if not(happy):
            newX = r.randint(-jumpsize, jumpsize)
            newY = r.randint(-jumpsize, jumpsize)
            newX += actorX
            newY += actorY
            if ((newX >= jumpsize) and (newX < nRows-jumpsize)
                and (newY >= jumpsize) and (newY < nCols - jumpsize)):
                if grid[newX][newY] == empty:
                    grid[newX][newY] = grid[actorX][actorY]
                    grid[actorX][actorY] = empty
    for x in xrange(nRows):
        for y in xrange(nCols):
            if grid[x][y] == empty:
                image(lilys, x*w, y*h, w, h)
            elif grid[x][y] == frog:
                image(frogs, x*w, y*h, w, h)
            elif grid[x][y] == turtle:
                image(turts, x*w, y*h, w, h)
            else:
                println("Etwas ist falsch im Staate Lilypond!")

            

def isHappy(animal, x, y):
    happy = 0
    if grid[x][y-1] == animal:
        happy += 1
    if grid[x+1][y-1] == animal:
        happy += 1
    if grid[x+1][y] == animal:
        happy += 1
    if grid[x+1][y+1] == animal:
        happy += 1
    if grid[x][y+1] == animal:
        happy += 1
    if grid[x-1][y+1] == animal:
        happy += 1
    if grid[x][y+1] == animal:
        happy += 1
    if grid[x-1][y] == animal:
        happy += 1
    if happy >= 3:
        return True
    else:
        return False
        
                
        
