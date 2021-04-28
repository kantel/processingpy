# Hommage an Bridget Riley 4
from random import randint, choice

WIDTH = 600
HEIGHT = 600
FPS = 60

riley = [color(235, 200, 55), color(115, 165, 215), color(155, 195, 80),
         color(230, 135, 170), color(230, 80, 70), color(65, 80, 150)] 
          
def setup():
    global counter, frontier
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Quadrate 2")
    stroke(255)
    strokeWeight(4)
    background(255)
    for j in range(10):
        for i in range(10):
            fill(choice(riley))
            rect(60*i, 60*j, 60, 60)
    counter = 0
    frontier = randint(45, 180)
    frameRate(FPS)

def draw():
    global counter, frontier
    for j in range(10):
        for i in range(10):
            if counter >= frontier:
                counter = 0
                frontier = randint(45, 180)
            if counter%frontier == 0:
                fill(choice(riley))
                rect(60*i, 60*j, 60, 60)
            counter += 1
    # if frameCount <= 3600:
    #     saveFrame("pics/####.png")
    # else:
    #     print("I did it Babe")
    #     noLoop()
    
    
