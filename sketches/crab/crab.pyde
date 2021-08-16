WIDTH = 640
HEIGHT = 480



def setup():
    global bg, crab
    size(WIDTH, HEIGHT)
    bg = loadImage("bg.png")
    crab = loadImage("crab.png")
    
def draw():
    background(49, 197, 244)
    image(bg, 0, 0)
    image(crab, width/2 - 30, height - 80)
