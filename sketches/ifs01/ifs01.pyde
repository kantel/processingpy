# Parameter
a = [0.0, 0.197, -0.155, 0.849]
b = [0.0, -0.226, 0.283, 0.037]
c = [0.0, 0.226, 0.26, -0.037]
d = [0.16, 0.197, 0.237, 0.849]
e = [0.0, 0.0, 0.0, 0.0]
f = [0.0, 1.6, 0.14, 1.6]

# Zufallsverteilung
p = [0.03, 0.14, 0.27, 1.0]

def setup():
    global x, y
    x, y = 0.0, 0.0
    size(640, 480)
    background(40, 40, 40)

def draw():
    global x, y
    pk = random(1.0)
    if pk <= p[1]:
        k = 1
    elif pk <= p[2]:
        k = 2
    elif pk <= p[3]:
        k = 3
    else:
        k = 4
    
    x1 = a[k]*x + b[k]*y + e[k]
    y = c[k]*x + d[k]*y + f[k]
    x = x1
    
    xp = round(x*50) + 280
    yp = 450 - round(y*40)
    
    # stroke(20, 255, 20)
    # strokeWeight(2)
    # print(x, y, k)
    set(xp, yp, color(20, 255, 20))
    if frameCount >= 10000:
        print("I did it, Babe!")
        noLoop()
    
    
