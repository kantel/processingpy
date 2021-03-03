add_library('Turtle')

# Konstanten-Deklaration
WIDTH = 400
HEIGHT = 200
it = 4          # Iterationstiefe

def setup():
    global koch
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Koch-Kurve")
    background(232, 226, 7)
    koch = Turtle(this)
    noLoop()

def draw():
    koch.penUp()
    koch.goToPoint(40, 140)
    stroke(200, 23, 223)
    koch.penDown()
    koch.right(90)
    kochkurve(400, it)
    print("I did it, Babe!")

def kochkurve(length, d):
    if d == 0:
        koch.forward(length)
    else:
        kochkurve(length/3, d-1)
        koch.left(60)
        kochkurve(length/3, d-1)
        koch.right(120)
        kochkurve(length/3, d-1)
        koch.left(60)
        kochkurve(length/3, d-1)
