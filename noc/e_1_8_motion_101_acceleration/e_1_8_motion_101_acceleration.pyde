from walker import Walker

def setup():
    global walker
    size(640, 360)
    this.surface.setTitle("Motion 101: Acceleration")
    walker = Walker()

def draw():
    background(98, 199, 119)
    walker.update()
    walker.checkEdges()
    walker.display()
