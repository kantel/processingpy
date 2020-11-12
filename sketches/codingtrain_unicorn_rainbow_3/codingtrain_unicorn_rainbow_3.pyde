from unicornrainbow import UnicornRainbow
from codingtrain import CodingTrain

trains = []
NO_TRAINS = 2

def setup():
    global unicorn, trains
    size(720, 360)
    this.surface.setTitle("Coding Train Unicorn Rainbow Stage 2")
    unicorn = UnicornRainbow()
    for i in range(NO_TRAINS):
        train = CodingTrain((i * 400) + 200)
        trains.append(train)

def draw():
    global unicorn, trains
    background(64)
    for train in trains:
        train.update()
        if train.reset:
            unicorn.score += 1
            print(unicorn.score)
    unicorn.add_rainbow_stripes()
    unicorn.update()
    for train in trains:
        train.show()
    unicorn.show()
    for train in trains:
        if train.rect_collision(unicorn):
            print("Game Over")
            noLoop()

def keyPressed():
    if (key == " "):
        unicorn.up()

def mousePressed():
    noLoop()  # Für Screenshot
