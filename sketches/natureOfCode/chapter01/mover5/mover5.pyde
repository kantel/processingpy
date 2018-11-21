from mover import Mover

numMovers = 20
movers = []

def setup():
    global mover
    size(640, 360)
    this.surface.setTitle("Mover 5")
    for _ in range(numMovers):
        movers.append(Mover())
        
def draw():
    background(235, 215, 182)
    
    for mover in movers:
        mover.update()
        mover.checkBoundaries()
        mover.display()
