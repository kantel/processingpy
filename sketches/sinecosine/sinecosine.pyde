# Sinus und Cosinus
import math

def setup():
    global a, b, co
    a = b = co = 0
    size(500, 400)
    background(255)
    colorMode(HSB, 100)
    strokeWeight(3)
    frameRate(30)

def draw():
    global a, b, co
    
    x0 = math.sin(a)*(width-20)/2
    y0 = math.cos(a)*(height-20)/2
    x1 = math.sin(b)*(width-20)/2
    y1 = math.cos(b)*(height-20)/2
    
    translate(width/2, height/2)
    stroke(co, 80, 80, 20)
    line(x0, y0, x1, y1)
    
    a += 0.02
    b += 0.05
    co += 1
    if co > 100:
        co = 0
    
    if frameCount%360 == 0:
        background(100)
        a = b = co = 0
        # frameCount = 0
        # print("I did it, Babe!")
        # noLoop()