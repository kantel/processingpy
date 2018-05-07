
def setup():
    global txt, y
    size(842, 480, P3D)  # große Version
    # size(560, 315, P3D) #kleine Version
    # fullScreen(P3D)
    y = height/2

    lines = loadStrings("manifest.txt")
    txt = join(lines, "\n")
    keepGoing = False


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
    
    saveFrame("output/manifest_####.png")
    
    y -= 1
    # print(y)
    if y <= -3300:
        keepGoing = False
        y = height/2
