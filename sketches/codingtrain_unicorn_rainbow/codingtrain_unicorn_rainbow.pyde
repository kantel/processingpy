from unicornrainbow import UnicornRainbow
from codingtrain import CodingTrain

def setup():
    global unicorn, train
    size(940, 360)
    this.surface.setTitle("Coding Train Unicorn Rainbow")
    unicorn = UnicornRainbow()
    train = CodingTrain()    

def draw():
    global unicorn, train
    background(64)
    train.update()
    unicorn.add_rainbow_stripes()
    unicorn.update()
    train.show()
    unicorn.show()
    
def mousePressed():
    noLoop() # Für Screenshot
