from amoeba import Amoeba

WIDTH = 960
HEIGHT = 540

FPS = 60
counter = 0

amoebas = []

for i in range(8):
    diameter = random(50, 150)
    x_speed = 1000/(diameter*(500*random(-2, 2)))
    if x_speed == 0:
        x_speed = 1000/(diameter*(500))
    y_speed = 1000/(diameter*(500*random(-2, 2)))
    if y_speed == 0:
        y_speed = 1000/(diameter*(500))
    radius = diameter/2
    x, y = random(radius, WIDTH - radius), random(radius, HEIGHT - radius)
    amoebas.append(Amoeba(x, y, diameter, x_speed, y_speed))

def setup():
    size(WIDTH, HEIGHT)
    this.surface.setTitle(u"Amöben in der Petrischale")
    frameRate(FPS)

def draw():
    background(132, 144, 163)
    for amoeba in amoebas:
        amoeba.update()
        amoeba.show()
        # collision detection
        for other in amoebas:
            if amoeba is other:
                continue
            distance = amoeba.location - other.location
            sum_radii = amoeba.d/2 + other.d/2
            if distance.mag() < sum_radii:
                amoeba.propulsion += distance.limit(0.05)
                other.propulsion -= distance.limit(0.05)
    # if frameCount <= 3600:
    #     saveFrame("pics/####.png")
    # else:
    #     print("I did it Babe")
    #     noLoop()
