import random as r

fps = 25
rep = 0
dem = 1
row = 10
col = 10
iconSize = 34
neighboorhood = []

def setup():
    frameRate(fps)
    size(row*iconSize, col*iconSize)
    repIcon = loadImage("rep.png")
    demIcon = loadImage("dem.png")
    i = 0
    while (i < row):
        j = 0
        while (j < col):
            rnd = r.randint(0, 1)
            if rnd == rep:
                neighboorhood[i][j] = rep
                image(repIcon, i*iconSize, j*iconSize)
            else:
                neighboorhood[i][j] = dem
                image(demIcon, i*iconSize, j*iconSize)
            j += 1
        i += 1

