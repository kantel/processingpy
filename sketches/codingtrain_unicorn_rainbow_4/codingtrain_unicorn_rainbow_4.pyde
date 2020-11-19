# The Coding Train designs and characters by Jason Heglund:
# https://jasonheglund.com/#/the-coding-train/

add_library('sound')
from unicornrainbow import UnicornRainbow
from codingtrain import CodingTrain

trains = []
NO_TRAINS = 2

def setup():
    global unicorn, trains, bg, fail, thisdot
    size(720, 360)
    this.surface.setTitle("Coding Train Unicorn Rainbow Final Stage")
    bg = loadImage("bg.jpg")
    # Font: https://fonts.google.com/specimen/Ranchers
    font = createFont("Ranchers-Regular.ttf", 30)
    textFont(font)
    unicorn = UnicornRainbow()
    for i in range(NO_TRAINS):
        train = CodingTrain((i * 400) + 200)
        trains.append(train)
    fail = SoundFile(this, "fail4.mp3")
    # This Dot Song by Kristian Pedersen:
    # https://soundcloud.com/kristianpedersen/this-dot-feat-daniel-shiffman
    # https://soundcloud.com/kristianpedersen
    thisdot = SoundFile(this, "this.mp3")
    thisdot.loop()

def draw():
    global unicorn, trains, bg, fail, thisdot
    background(bg)
    for train in trains:
        train.update()
        if train.reset:
            unicorn.score += 1
            # print(unicorn.score)
    unicorn.add_rainbow_stripes()
    unicorn.update()
    for train in trains:
        train.show()
    unicorn.show()
    for train in trains:
        if train.rect_collision(unicorn):
            thisdot.stop()
            fail.play()
            # print("Game Over")
            noLoop()
    fill(129, 122, 198)
    textSize(30)
    text("Score: " + str(unicorn.score), 15, 40)

def keyPressed():
    if (key == " "):
        unicorn.up()
