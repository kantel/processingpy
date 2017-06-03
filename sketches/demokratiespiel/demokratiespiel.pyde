import random as r

rep = 0
dem = 1
nReps = nDems = 0
nCols  = nRows = 20
w = h = 34

def setup():
    global grid, reps, dems, nReps, nDems
    size(680, 680)
    reps = loadImage("rep.png")
    dems = loadImage("dem.png")
    grid = []
    for x in xrange(nRows):
        grid.append([])
        for y in xrange(nCols):
            grid[x].append(r.randint(0, 1))
            if grid[x][y] == rep:
                nReps += 1
                image(reps, x*w, y*w, w, h)
            else:
                image(dems, x*w, y*w, w, h)
                nDems += 1
    println("Start: Demokraten = " + str(nDems) + ", Republikaner = " + str(nReps))

def draw():
    global reps, dems, nReps, nDems
    actorX = r.randint(0, nRows - 1)
    actorY = r.randint(0, nCols - 1)
    selection = r.randint(0, 7)
    if selection == 0:
        neighboorX = actorX
        neighboorY = actorY - 1
    elif selection == 1:
        neighboorX = actorX + 1
        neighboorY = actorY - 1
    elif selection == 2:
        neighboorX = actorX + 1
        neighboorY = actorY
    elif selection == 3:
        neighboorX = actorX + 1
        neighboorY = actorY + 1
    elif selection == 4:
        neighboorX = actorX
        neighboorY = actorY + 1
    elif selection == 5:
        neighboorX = actorX - 1
        neighboorY = actorY + 1
    elif selection == 6:
        neighboorX = actorX - 1
        neighboorY = actorY
    elif selection == 7:
        neighboorX = actorX - 1
        neighboorY = actorY - 1
    else:
        println("Irgend etwas ist gewaltig schiefgelaufen!")
    
    # Prüfung der Ränder:
    if neighboorX < 0:
        neighboorX = nRows + neighboorX
    neighboorX = neighboorX % nRows
    if neighboorY < 0:
        neighboorY = nCols + neighboorY
    neighboorY = neighboorY % nCols
    
    # Neuzeichnen des Spielfelds:
    if grid[neighboorX][neighboorY] == dem:
        if grid[actorX][actorY] != dem:
            nDems += 1
            nReps -= 1
        grid[actorX][actorY] = dem
        image(dems, actorX*w, actorY*w, w, h)
    else:
        if grid[actorX][actorY] != rep:
            nReps += 1
            nDems -= 1
        grid[actorX][actorY] = rep
        image(reps, actorX*w, actorY*w, w, h)
    println("Runde " + str(frameCount) + ": Demokraten = " + str(nDems) + ", Republikaner = " + str(nReps))
    
    if nDems == 0:
        println("Die Republikaner haben nach " + str(frameCount) + u" Runden die Macht übernommen!")
        noLoop()
    if nReps == 0:
        println("Die Demokraten haben nach " + str(frameCount) + u" Runden die Macht übernommen!")
        noLoop()
