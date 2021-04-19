WIDTH = 600
HEIGHT = 600
FPS = 60
MAX_TIME = 120

from color_list import pygame_colors
from rgb_list import pygame_all_rgb

def setup():
    global timer, index
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Pygame Colors")
    font = createFont("American Typewriter", 40)
    textAlign(CENTER)
    textFont(font)
    index = 0
    timer = 0
    frameRate(FPS)
    print(len(pygame_all_rgb))

def draw():
    global timer, index
    background(234, 218, 184) # Packpapier
    fill(0, 150, 0)
    noStroke()
    text(pygame_colors[index][0], width/2, 60)
    text(str(pygame_all_rgb[index]), width/2, 560)
    stroke(0)
    strokeWeight(5)
    fill(pygame_colors[index][1])
    circle(width/2, height/2, 400)
    if timer >= MAX_TIME:        
        timer = 0
        index += 1
        print(str(index))
        if index >= len(pygame_all_rgb):
            print("I did it, Babe!")
            noLoop()
    timer += 1
