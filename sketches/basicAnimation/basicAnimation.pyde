lgreen = "#63e06b"
dgreen = "#217424"
yellow = "#ffd05e"
lblue  = "#40b0e2"
white  = "#ffffff"

x1 = -200 # große Hügel
x2 = 200
x3 = 600

x4 = 400 # Wolke

x5 = -200 # kleine Hügel
x6 = 0
x7 = 200
x8 = 400
x9 = 600
x10 = 800

alienx = -66 #Alien
alieny = 308

step0 = 1
step1 = 2
step2 = 3
step3 = 4

def setup():
    global alien
    size(800, 450)
    this.surface.setTitle("Basic Animation")
    alien = loadImage("alien.png")
    noStroke()


def draw():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, alienx
    background(lblue)

    fill(white) # Wolke
    circle(x4, 150, 100)
    circle(x4, 200, 100)
    circle(x4 - 50, 200, 100)
    circle(x4 + 50, 200, 100)
        
    fill(lgreen) # große Hügel
    circle(x1, 400, 400)
    circle(x2, 400, 400)
    circle(x3, 400, 400)
    
    fill(dgreen) # kleine Hügel
    circle(x5, 400, 200)
    circle(x6, 400, 200)
    circle(x7, 400, 200)
    circle(x8, 400, 200)
    circle(x9, 400, 200)
    circle(x10, 400, 200)
    
    fill(yellow) # ground
    rect(0, 400, 800, 50)
    
    image(alien, alienx, alieny)
    

    # Bewege die Wolke
    x4 += step0
    if x4 >= 1000:
        x4 = - 200
    
    # Bewege die hinteren Hügel        
    x1 += step1
    x2 += step1
    x3 += step1
    
    if x1 >= 1000:
        x1 = -200
    if x2 >= 1000:
        x2 = -200
    if x3 >= 1000:
        x3 = -200
    
    # Bewege die vorderen Hügel
    x5 += step2
    x6 += step2
    x7 += step2
    x8 += step2
    x9 += step2
    x10 += step2
    
    if x5 >= 900:
        x5 = -100
    if x6 >= 900:
        x6 = -100
    if x7 >= 900:
        x7 = -100
    if x8 >= 900:
        x8 = -100
    if x9 >= 900:
        x9 = -100
    if x10 >= 900:
        x10 = -100
   
    # Bewege das Alien
    alienx += step3
    if alienx >= 866:
        alienx = -66
