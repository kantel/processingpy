r1 = 300.0  # Radius großer Kreis (width/2)
r2 = 175.0  # Radius innerer Kreis
r3 = 5.0    # Radius malender »Punkt«

p1 = 0.9
p2 = 0.25

# Großer Kreis
x1 = 0
y1 = 0
t = 0
points1 = []
points2 = []

def setup():
    size(600, 600)
    this.surface.setTitle("Spirograph mit zwei Stiften")

def draw():
    global r1, r2, x1, y1, t, p1, p2, points1, points2
    translate(width/2, height/2)
    background(235, 215, 182)  # Packpapier
    noFill()
    
    # Großer Kreis
    strokeWeight(1)
    stroke(0, 0, 200)  # Blau
    ellipse(x1, y1, 2*r1, 2*r1)
    
    # Innerer Kreis
    stroke(0, 200, 0)  # Grün
    x2 = (r1 - r2)*cos(t)
    y2 = (r1 - r2)*sin(t)
    ellipse(x2, y2, 2*r2, 2*r2)
    
    # Malender Punkt 1
    x3 = x2 + p1*(r2 - r3)*cos(-((r1 - r2)/r2)*t)
    y3 = y2 + p1*(r2 - r3)*sin(-((r1 - r2)/r2)*t)
    fill(200, 0, 0)  # Rot
    ellipse(x3, y3, 2*r3, 2*r3)
    
    # Malender Punkt 2
    x4 = x2 - p2*(r2 - r3)*cos(-((r1 - r2)/r2)*t)
    y4 = y2 - p2*(r2 - r3)*sin(-((r1 - r2)/r2)*t)
    fill(0, 0, 200)  # Blau
    ellipse(x4, y4, 2*r3, 2*r3)

    # Liste der zu zeichnenden Punkte
    points1 = [[x3, y3]] + points1[:2000]
    points2 = [[x4, y4]] + points2[:2000]
    noFill()
    strokeWeight(2)
    with beginShape():
        for pt1 in points1:
            stroke(200, 0, 0)  # Rot
            vertex(pt1[0], pt1[1])
    with beginShape():
        for pt2 in points2:
            stroke(0, 0, 200)  # Blau
            vertex(pt2[0], pt2[1])

    t += 0.05
