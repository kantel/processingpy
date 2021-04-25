# Hommage an Bridget Riley 3
from random import choice

WIDTH = 600
HEIGHT = 600
FPS = 60

riley = [color(235, 200, 55), color(115, 165, 215), color(155, 195, 80),
         color(230, 135, 170), color(230, 80, 70), color(65, 80, 150)] 
          
def setup():
    global counter
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Hommage an Bridget Riley: Quadrate")
    stroke(255)
    strokeWeight(4)
    background(255)
    counter = 0
    frameRate(FPS)

def draw():
    global counter
    if counter >= FPS:
        counter = 0
    if counter%FPS == 0:
        for j in range(10):
            for i in range(10):
                fill(choice(riley))
                rect(60*i, 60*j, 60, 60)
    counter += 1
    
    
