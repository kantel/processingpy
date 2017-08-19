from random import randint
from sprite import Skull, Smiley

w = 640
tw = th = 36
noSmileys = 10

skull = Skull(w/2, 400)
smiley = []
for i in range(noSmileys):
    smiley.append(Smiley(randint(0, w-tw), randint(50, 250)))

def setup():
    skull.score = 0
    size(640, 480)
    frameRate(30)
    skull.loadPics()
    for i in range(len(smiley)):
        smiley[i].loadPics()
        smiley[i].dy = randint(2, 10)
    font = loadFont("ComicSansMS-32.vlw")
    textFont(font, 32)
    noCursor()
    # cursor(HAND)
  
def draw():
    background(0, 0, 0)
    text("Score: " + str(skull.score), 10, 32)
    skull.move()
    skull.display()
    for i in range(len(smiley)):
        smiley[i].move()
        if smiley[i].over:
            skull.score += 1
        smiley[i].display()