def setup():
    size(720, 500)
    this.surface.setTitle(u"Mysteriöses Moiré")

def draw():
    background(220)
    x = 0
    # x = width/2
    noFill()
    
    for i in range(0, 1500, 3):
        mycolor = color(150, 100, 255)
        strokeWeight(2)
        stroke(mycolor)
        ellipse(360, 250, i, i)
        mycolor = color(255, 0, 0)
        strokeWeight(1)
        stroke(mycolor)
        if i%2:
            ellipse(x, 250, i-500, i-500)
    if x > width:
        x = 0
    else:
        x += 5
