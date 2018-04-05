# Parameter
a = [0.195, 0.462, -0.058, -0.035, -0.637]
b = [-0.488, 0.414, -0.07, 0.07, 0.0]
c = [0.344, -0.252, 0.453, -0.469, 0.0]
d = [0.443, 0.361, -0.111, -0.022, 0.501]
e = [0.4431, 0.2511, 0.5976, 0.4884, 0.8562]
f = [0.2453, 0.5692, 0.0969, 0.5069, 0.2513]
# f = [0.0, 1.6, 0.44, 1.6]

# Zufallsverteilung
p = [0.1, 0.15, 0.2, 0.25, 1.0]
# p = [0.074, 0.08, 0.09, 1.0]
def setup():
    global x, y
    x, y = 0.0, 0.0
    size(640, 480)
    background(40, 40, 40)

def draw():
    global x, y
    
    for i in range(250):
        pk = random(1.0)
        if pk <= p[1]:
            k = 1
        elif pk <= p[2]:
            k = 2
        elif pk <= p[3]:
            k = 3
        elif pk <= p[4]:
            k = 4
        else:
            k = 5
    
        x1 = a[k]*x + b[k]*y + e[k]
        y = c[k]*x + d[k]*y + f[k]
        x = x1
    
        xp = round(x*500) + width/8
        yp = 450 - round(y*500)
    
        set(xp, yp, color(20, 255, 20))
        
    if frameCount >= 250:
        print("I did it, Babe!")
        noLoop()
    
    
