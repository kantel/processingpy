from random import randint

WIDTH, HEIGHT = 400, 400

def setup():
    global walker, r, g, b
    size(WIDTH, HEIGHT)
    this.windowTitle("Random Walker")
    # x, y = width/2, height/2
    walker = PVector(width/2, height/2)

    r = randint(20, 200)
    g = randint(20, 200)
    b = randint(20, 200)
    strokeWeight(2)
    
    background(235, 215, 182)  # Packpapier
    
    
def draw():
    for i in range(100):
        step()

def step():
    global walker, r, g, b
    
    walker.x += randint(-1, 1)
    walker.y += randint(-1, 1)
    walker.x = constrain(walker.x, 10, width - 10)
    walker.y = constrain(walker.y, 10, height - 10)
    
    r += randint(-1, 1)
    g += randint(-1, 1)
    b += randint(-1, 1)
    r = constrain(r, 20, 200)
    g = constrain(g, 20, 200)
    b = constrain(b, 20, 200)
    
    a = 100
    stroke(r, g, b, a)
    point(walker.x, walker.y)
    
     
