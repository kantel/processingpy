# Pythagorasbaum
# Den rekursiven Algorithmus habe ich einem Pascal-Programm aus
# Jürgen Plate: Computergrafik: Einführung – Algorithmen –
# Programmentwicklung, München (Franzis) 2. Auflage 1988,
# Seiten 460-462 entnommen.

palette = [color(189,183,110), color(0,100,0), color(34,139,105),
           color(152,251,152), color(85,107,47), color(139,69,19),
           color(154,205,50), color(107,142,35), color(139,134,78),
           color(139, 115, 85)]

xmax = 600
xmitte = 300
ymax = 440

level = 12
w1 = 0.36   # Winkel 1
w2 = 0.48   # Winkel 2

# Setzt man beide Winkel auf 0.5, erhält man den geraden Pythagoras-Baum
# w1 = 0.5
# w2 = 0.5

def setup():
    size(640, 480)
    frame.setTitle("Arbor Pythagorae")
    background(255)
    strokeWeight(1)
    noLoop()

def draw():
    drawPythagoras(-(xmax/10), 0, xmax/20, 0, level)

def drawPythagoras(a1, a2, b1, b2, level):
    if (level > 0):
        # Eckpunkte berechnen
        n1 = -b2 + a2
        n2 = -a1 + b1
        c1 = b1 + n1
        c2 = b2 + n2
        d1 = a1 + n1
        d2 = a2 + n2
        # Start-Rechteck zeichnen
        fill(palette[(level-1)%10])
        with beginClosedShape():
            vertex(a1 + xmitte, ymax - a2)
            vertex(b1 + xmitte, ymax - b2)
            vertex(c1 + xmitte, ymax - c2)
            vertex(d1 + xmitte, ymax - d2)
        e1 = d1 + w1*(c1 - d1) + w2*n1
        e2 = d2 + w1*(c2 - d2) + w2*n2
        # Schenkel-Quadrate zeichnen
        drawPythagoras(e1, e2, c1, c2, level-1)
        drawPythagoras(d1, d2, e1, e2, level-1)

                        
                        