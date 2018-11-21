from mover import Mover

def setup():
    global mover
    size(640, 360)
    this.surface.setTitle("Mover 2")
    mover = Mover()

def draw():
    background(235, 215, 182)
    
    mover.update()
    mover.checkBoundaries()
    mover.display()
