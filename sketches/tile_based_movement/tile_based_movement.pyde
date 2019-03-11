TILESIZE = 32
from orc import Orc

orc = Orc(3, 3)

def setup():
    size(320, 320)
    this.surface.setTitle("Tile Based Movement")
    orc.loadPics()

def draw():
    background(100, 150, 0)
    drawGrid()
    orc.move()
    orc.display()

def drawGrid():
    stroke(255)
    for i in range(0, width, TILESIZE):
        line(i, 0, i, height)
    for i in range(0, height, TILESIZE):
        line(0, i, width, i)
        
def keyPressed():
    if keyPressed and key == CODED:
        if orc.frame == 0:
            if keyCode == RIGHT:
                orc.from_x = orc.x
                orc.from_y = orc.y
                if orc.x >= ((width - TILESIZE)/TILESIZE):
                    orc.x = orc.from_x
                    orc.frame = 0
                else:
                    orc.x += 1
                    orc.frame = 1
                orc.dir = "right"
            elif keyCode == LEFT:
                orc.from_x = orc.x
                orc.from_y = orc.y
                if orc.x <= 0:
                    orc.x = orc.from_x
                    orc.frame = 0
                else:
                    orc.x -= 1
                    orc.frame = 1
                orc.dir = "left"
            elif keyCode == UP:
                orc.from_x = orc.x
                orc.from_y = orc.y
                if orc.y <= 0:
                    orc.y = orc.from_y
                    orc.frame = 0
                else:
                    orc.y -= 1
                    orc.frame = 1
                orc.dir = "up"
            elif keyCode == DOWN:
                orc.from_x = orc.x
                orc.from_y = orc.y
                if orc.y >= ((height - TILESIZE)/TILESIZE):
                    orc.y = orc.from_y
                    orc.frame = 0
                else:
                    orc.y += 1
                    orc.frame = 1 
                orc.dir = "down"
                
            
