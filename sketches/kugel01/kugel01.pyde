def setup():
    size(200, 200, P3D)

def draw():
    background(160)
    lights()
    translate(width/2, height/2, 0)
    rotateX(mouseY*0.025)
    rotateZ(mouseX*0.025)
    sphereDetail(30)
    sphere(80)
