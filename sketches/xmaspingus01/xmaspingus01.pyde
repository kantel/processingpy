# xmaspingus01

from sprite3 import Pingus
tilew = 32
tileh = 44



def setup():
    global bg
    
def draw():
    background(bg)
    
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
            
