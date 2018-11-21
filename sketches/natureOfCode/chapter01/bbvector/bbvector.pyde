r = 15

def setup():
    global location, velocity
    size(640, 360)
    this.surface.setTitle("Bouncing Ball with PVectors")
    location = PVector(100, 100)
    velocity = PVector(2.5, 5)

def draw():
    background(235, 215, 182)
    location.add(velocity)
    # check boundaries
    if (location.x > width - r) or (location.x < r):
        velocity.x = velocity.x * -1
    if (location.y > height - r) or (location.y < r):
        velocity.y = velocity.y * -1
    
    stroke(0)
    fill(255, 100, 255)
    ellipse(location.x, location.y, 2*r, 2*r)
