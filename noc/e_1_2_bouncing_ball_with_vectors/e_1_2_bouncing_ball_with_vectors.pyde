d = 20

def setup():
    global location, velocity
    size(640, 360)
    this.surface.setTitle("Bouncing Ball with Vectors")
    location = PVector(100, 100)
    velocity = PVector(2.5, 5)

def draw():
    global location, velocity
    background(98, 199, 119)
    location.add(velocity)
    if (location.x > width - d/2) or (location.x < d/2):
        velocity.x *= -1
    if (location.y > height - d/2) or (location.y < d/2):
        velocity.y *= -1
    
    stroke(0)
    fill(240, 80, 37)
    circle(location.x, location.y, d)
