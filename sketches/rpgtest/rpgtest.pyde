def setup():
    global hero, ground01
    size(512, 512)
    
    hero = loadImage("knt1_bk1.gif")
    ground01 = loadImage("ground01.png")

def draw():
    background(0, 0, 0)
    
    fill(0, 200, 0)
    # noStroke()
    # rect(0, 80, width, 352)
    image(ground01, 0, 80)

    image(hero, 320, 280)
    
