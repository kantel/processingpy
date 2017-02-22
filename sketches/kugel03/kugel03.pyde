a = 0

def setup():
    global globe
    earth = loadImage("earth.jpg")
    size(400, 400, P3D)
    noStroke()
    globe = createShape(SPHERE, 160)
    globe.setTexture(earth)

def draw():
    global a, globe
    background(51)
    lights()
    translate(width*.5, height*.5, 0)
    # sphereDetail(120)
    with pushMatrix():
        rotateX(radians(-25))
        rotateY(a)
        a += 0.01
        shape(globe)