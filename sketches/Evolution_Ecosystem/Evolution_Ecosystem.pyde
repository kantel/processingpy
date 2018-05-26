from world import World

def setup():
    global world
    size(600, 400)
    world = World(20)
    frameRate(30)

def draw():
    global world
    # background("#1f2838")
    background(255)
    world.run()
