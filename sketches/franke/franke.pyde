from random import randint

this.surface.setTitle("Re-Enactment Herbert W. Franke")
size(400, 600)
background(240, 220, 200)
magenta  = color(247, 114, 205)
orange   = color(252, 188, 117)
darkgrey = color(84, 72, 74)
rectMode(CENTER)
strokeWeight(2)
noFill()
for _ in range(100):
    margin = 25
    stroke(orange)
    x = randint(margin, width - margin)
    y = randint(4*margin, height - 4*margin)
    rect(x, y, margin, margin)
for _ in range(150):
    margin = 8
    stroke(magenta)
    x = randint(margin, width - margin)
    y = randint(12*margin, height - 12*margin)
    rect(x, y, margin, margin)
for _ in range(4):
    margin = 100
    stroke(darkgrey)
    x = randint(margin/2, width - margin/2)
    y = randint(margin + 5, height - margin - 5)
    rect(x, y, margin, margin)
