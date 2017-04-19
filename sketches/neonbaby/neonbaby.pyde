from random import randint

neon1 = [color(230, 96, 55), color(183, 116, 64), color(212, 251, 69),
         color(252, 75, 200), color(159, 53, 233), color(57, 218, 56),
         color(67, 253, 133), color(78, 148, 42), color(67, 254, 211),
         color(74, 143, 186), color(52, 99, 234), color(17, 42, 106)]

def setup():
    size(600, 600)
    frame.setTitle("Neonbaby")
    background(0)
    
def draw():
    x = random(width)
    y = random(height)
    dia = random(5, 25)
    mycolor = neon1[randint(0, 11)]
    fill(mycolor)
    ellipse(x, y, dia, dia)