t = 0
r2 = 5
p = 10 # Periode
offset = 250
circleList = []

def setup():
    size(960, 400)
    this.surface.setTitle("Fourier 2 (Fourier-Reihe)")

def draw():
    global t, circleList
    background(200)
    translate(offset, height / 2)

    x = 0
    y = 0
    strokeWeight(1)
    for i in range(p):
        prevx = x
        prevy = y
        
        n = i * 2 + 1
        r1 = 100 * (4 / (n * PI))
        x += r1 * cos(n * t)
        y += r1 * sin(n * t)

        # Großer Kreis
        noFill()
        stroke(0)
        ellipse(prevx, prevy, 2 * r1, 2 * r1)

        # Linie vom großen zum kleinen Kreis
        line(prevx, prevy, x, y)

        # Kleiner Kreis
        fill(200, 0, 0)  # Rot
        ellipse(prevx, prevy, 2 * r2, 2 * r2)
    
    circleList = [y] + circleList[:450]
    
    # Linie
    fill(200, 0, 0)
    ellipse(x, y, 2 * r2, 2 * r2)
    stroke(0, 0, 200) # Blau für die Linie
    line(x, y, offset, y)
    noStroke()
    fill(0, 200, 0) # Grün
    ellipse(offset, y, 2*r2, 2*r2)
    
    with beginShape():
        noFill()
        strokeWeight(2)
        stroke(0, 200, 0) # Grün
        for i, c in enumerate(circleList):
            vertex(offset + i, c)

    t += .02
