speed = 0.5

def setup():
    global balloon, x, y
    size(400, 200)
    balloon = loadImage("1f388.png")
    x = random(0, width-144)
    y = height

def draw():
    global balloon, x, y
    background(255)
    image(balloon, x, y)
    y -= speed
    if (y < -72):
        y = height
        x = random(0, width)
    
    