# Running Orc 02
from sprite2 import Orc, Wall, Lava
tilesize = 32


obstacles = [[9,9,9,9,9,9,9,9,0,9],
             [9,0,0,0,9,0,0,0,0,9],
             [9,9,0,0,0,0,0,0,0,9],
             [8,9,9,9,0,0,9,9,9,9],
             [9,9,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,9],
             [9,0,9,9,9,0,0,9,9,9],
             [9,0,9,0,0,0,0,0,9,8],
             [9,9,9,9,0,9,0,0,9,8],
             [8,8,8,9,0,9,9,9,9,8]]

orc = Orc(8*tilesize, 0)
wall = []
lava = []

def setup():
    global bg
    # bg = loadImage("ground0.png")
    bg = loadImage("ground.png")
    loadObstaclesData()
    # for i in range(len(wall)):
    #     wall[i].loadPics()
    # for i in range(len(lava)):
    #     lava[i].loadPics()
    frameRate(30)
    size(320, 320)
    orc.loadPics()
    orc.dx = 2
    orc.dy = 2
    
def draw():
    background(bg)
    # for i in range(len(wall)):
    #     wall[i].display()
    # for i in range(len(lava)):
    #     lava[i].display()
    orc.move()
    for i in range(len(wall)):
        if orc.checkCollision(wall[i]):
            if orc.dir == 0:
                orc.x -= orc.dx
            elif orc.dir == 1:
                orc.y -= orc.dy
            elif orc.dir == 2:
                orc.x += orc.dx
            elif orc.dir == 3:
                orc.y += orc.dy
            orc.image1 = orc.image2                            
    orc.display()
    
def keyPressed():
    if keyPressed and key == CODED:
        if keyCode == RIGHT:
            orc.dir = 0
        elif keyCode == DOWN:
            orc.dir = 1
        elif keyCode == LEFT:
            orc.dir = 2
        elif keyCode == UP:
            orc.dir = 3
            
def loadObstaclesData():
    for y in range(10):
        for x in range(10):
            if obstacles[y][x] == 9:
                wall.append(Wall(x*tilesize, y*tilesize))
            elif obstacles[y][x] == 8:
                lava.append(Lava(x*tilesize, y*tilesize))
