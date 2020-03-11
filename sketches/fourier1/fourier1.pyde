r1 = 100
r2 = 5
t = 0
circleList = []

def setup():
    size(800, 400)
    this.surface.setTitle("Fourier 1 (Fourier Sinus)")

def draw():
    global t, circleList
    background(200)
    translate(width / 4, height / 2)

    # Großer Kreis
    noFill()
    stroke(0)
    ellipse(0, 0, 2 * r1, 2 * r1)

    # Kleiner Kreis
    fill(200, 0, 0)  # Rot
    y = r1 * sin(t)
    x = r1 * cos(t)
    circleList = [y] + circleList[:360]
    ellipse(x, y, 2 * r2, 2 * r2)

    # Linie vom großen zum kleinen Kreis
    line(0, 0, x, y)

    # Linie
    stroke(0, 0, 200)  # Blau für die Linie
    line(x, y, 200, y)
    noStroke()
    fill(0, 200, 0)  # Grün
    ellipse(200, y, 2 * r2, 2 * r2)

    fill(0, 200, 0)  # Grün
    for i, c in enumerate(circleList):
        ellipse(200 + i, c, 3, 3)

    t += .02
