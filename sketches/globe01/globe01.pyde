a = 0.0

def setup():
    global globe
    size(400, 400, P3D)
    globe = makeSphere(150, 10)

def draw():
    global globe, a
    background(0)
    translate(width/2, height/2)
    with pushMatrix():
        # rotateX(radians(0))
        rotateY(a)
        a += 0.01
        shape(globe)

def makeSphere(r, step):
    s = createShape()
    s.beginShape(QUAD_STRIP)
    # s.beginShape(TRIANGLE_STRIP)
    s.noFill()
    s.stroke(255)
    s.strokeWeight(1)
    i = 0
    while i < 180:
        sini = sin(radians(i))
        cosi = cos(radians(i))
        sinip = sin(radians(i + step))
        cosip = cos(radians(i + step))
        j = 0
        while j <= 360:
            sinj = sin(radians(j))
            cosj = cos(radians(j))
            s.vertex(r*cosj*sini, r*-cosi, r*sinj*sini)
            s.vertex(r*cosj*sinip, r*-cosip, r*sinj*sinip)
            j += step
        i += step
    s.endShape()
    return s