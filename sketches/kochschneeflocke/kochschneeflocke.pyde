add_library('Turtle')

# Konstanten-Deklaration
WIDTH = 400
HEIGHT = 400

colors = [color(18, 184, 116), color(200, 23, 223),
          color(95, 145, 40), color(8, 124, 127)]

seiten = 4      # Anzahl der Seiten der Schneeflocke,
                # entweder 3 oder 4
it = 5          # Iterationstiefe

def setup():
    global koch
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Kochsche Schneeflocke")
    background(232, 226, 7)
    koch = Turtle(this)
    noLoop()

def draw():
    koch.penUp()
    koch.goToPoint(80, 320)
    koch.penDown()
    # koch.right(90)
    schneeflocke(400, it)
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

def schneeflocke(length, d):
    for i in range(seiten):
        stroke(colors[i%4])
        kochkurve(length, d)
        koch.right(360/seiten)
