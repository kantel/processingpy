a = 0

def setup():
    size(200, 200, P3D)

def draw():
    global a
    background(160)
    lights()
    translate(width/2, height/2, 0)
    sphereDetail(30)
    with pushMatrix():
        rotateX(radians(-10))
        rotateY(a)
        a += 0.01
        sphere(80)