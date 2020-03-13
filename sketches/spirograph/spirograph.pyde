r1 = 300.0  # Radius großer Kreis (width/2)
r2 = 110.0  # Radius innerer Kreis
r3 = 5.0    # Radius malender »Punkt«

p = 0.75

# Großer Kreis
x1 = 0
y1 = 0
t = 0
points = []

def setup():
    size(600, 600)
    this.surface.setTitle("Spirograph")

def draw():
    global r1, r2, x1, y1, t, p, points
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
    
    # Malender Punkt
    x3 = x2 + p*(r2 - r3)*cos(-((r1 - r2)/r2)*t)
    y3 = y2 + p*(r2 - r3)*sin(-((r1 - r2)/r2)*t)
    fill(200, 0, 0)  # Rot
    ellipse(x3, y3, 2*r3, 2*r3)
    
    # Liste der zu zeichnenden Punkte
    points = [[x3, y3]] + points[:2000]
    with beginShape():
        noFill()
        strokeWeight(2)
        stroke(200, 0, 0)  # Rot
        for pt in points:
            vertex(pt[0], pt[1])

            
    
    t += 0.05
