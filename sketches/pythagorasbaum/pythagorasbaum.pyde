# Symmetrischer Pythagorasbaum
# Nach einem Pascal-Programm aus: Dietmar Herrmann: Algorithmen für Chaos und Fraktale,
# Bonn (Addison-Wesly) 1994, S. 168-170

c = 0.707107  # 1/sqrt(2)
palette = [color(139,69,19), color(169, 69,19), color(139, 115, 85),
           color(139,134,78), color(107,142,35), color(154,205,50),
           color(189,183,110), color(85,107,47), color(152,251,152),
           color(34,139,105), color(0,100,0)]
h10 = 48    # height/10 
fk = 6.5    # Skalierungsfaktor

def setup():
    size(640, 480)
    background(255)
    strokeWeight(1)
    noLoop()

def draw():
    d = []
    u = v = 1.0
    for m in range(0, 11):
        p = 1
        for k in range(1, m):
            p = 2*p
            for n in range(p, 2*p-1):
                l = n
                h = 1
                for k in range(1, m-1):
                    print(m-k),
                    # d.append(l%2)
                    d[-k] = l%2
                    l = l/2
                x = y = f = 0.0
                for j in range(2, m):
                    if d[j] == 0:
                        x -= h*(cos(f) + 2*sin(f))
                        y += h*(2*cos(f) - sin(f))
                        f += PI/4
                    else:
                        x += h*(cos(f) - 2*sin(f))
                        y += h*(2*cos(f) + sin(f))
                        f -= PI/4
                    h = c*h
                u = h*(cos(f) + sin(f))
                v = h*(cos(f) - sin(f))
                beginShape()
                fill(palette[m])
                vertex(h10*(x - v + fk), height-(h10*(y - u + 2)))
                vertex(h10*(x + u + fk), height-(h10*(y - v + 2)))
                vertex(h10*(x + v + fk), height-(h10*(y + u + 2)))
                vertex(h10*(x - u + fk), height-(h10*(y - v + 2)))
                vertex(h10*(x - v + fk), height-(h10*(y - u + 2)))
                endShape(CLOSE)
                        
                        