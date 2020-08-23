from random import randint, choice

a = 220
colors = [color(155, 46, 105, a), color(217, 55, 80, a), color(226, 114, 79, a),
          color(243, 220, 123, a), color(78, 147, 151, a)]

def setup():
    size(940, 300)
    rectMode(CENTER)
    strokeWeight(2)
    # noStroke()
    background(255)

def draw():
    for _ in range(200):
        fill(choice(colors))
        rect(randint(0, width), randint(0, height), randint(10, width - 200),
             randint(10, int((height/2) - 100)))
    noLoop()
