
def setup():
    global txt, y
    size(800, 600, P3D)
    y = height/2

    lines = loadStrings("manifest.txt")
    txt = join(lines, "\n")


def draw():
    global txt, y
    background(0)
    translate(width/2, height/2)

    fill(238, 213, 75)
    textSize(width*0.04)
    textAlign(CENTER)
    rotateX(PI/4)
    w = -width*0.6
    text(txt, -w/2, y, w, height*10)
    
    y -= 1
    if y <= -3300:
        y = height/2
