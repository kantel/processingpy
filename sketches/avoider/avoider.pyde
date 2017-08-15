from random import randint
from sprite import Skull, Smiley

w = 640
tw = th = 36

skull = Skull(w/2, 400)
smiley = Smiley(randint(0, w-tw), randint(50, 250))

def setup():
    size(640, 480)
    frameRate(30)
    skull.loadPics()
    smiley.loadPics()
    smiley.dy = 10
  
def draw():
    background(0, 0, 0)
    skull.move()
    skull.display()
    smiley.move()
    smiley.display()
