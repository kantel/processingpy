myMagma = ['#000003', '#140D35', '#3B0F6F', '#63197F', '#8C2980', '#B53679', '#DD4968',
           '#F66E5B', '#FD9F6C', '#FDCD90', '#FBFCBF']
n = 0
c = 6

def setup():
    size(800, 600)
    this.surface.setTitle("Phyllotaxis 1")
    background(235, 215, 182)

def draw():
    global n
    a = n * radians(137.5)
    r = c * sqrt(n)
    x = r*cos(a)
    y = r*sin(a)
    
    fill(myMagma[(n%5) + 3])
    translate(width/2, height/2)
    circle(x, y, 8)
    n += 1
    if n > 2095:
        print("I did it, Babe!")
        noLoop()
