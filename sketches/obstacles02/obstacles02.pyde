# obstacles

tileSize = 32

from sprites import Orc, Wall, Tree
moving = True


def setup():
    global bg
    bg = loadImage("ground0.png")
    frameRate(30)
    size(320, 320)
    global orc
    orc = Orc(8*tileSize, 0)
    orc.loadPics()
    orc.dx = 2
    orc.dy = 2
    global wall1
    wall1 = Wall(5*tileSize, 3*tileSize)
    wall1.loadPics()
    global tree1
    tree1 = Tree(3*tileSize, 7*tileSize)
    tree1.loadPics()

def draw():
    global moving
    background(bg)
    wall1.display()
    tree1.display()
    orc.move()
    if orc.checkCollision(wall1) or orc.checkCollision(tree1):
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