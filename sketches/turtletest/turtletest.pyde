add_library('Turtle')

def setup():
    global t
    size(250, 250)
    this.surface.setTitle(u"Schildkröte")
    background(255)
    stroke(0)
    t = Turtle(this)
    noLoop()

def draw():
    global t
    # Zeichne ein Quadrat
    for _ in range(4):
        t.right(90)
        t.forward(100)
    print("I did it, Babe!")
