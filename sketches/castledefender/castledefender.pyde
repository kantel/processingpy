import math
from castle import Castle
from bullet import Bullet

WIDTH = 900
HEIGHT = 600
FPS = 60

bullets = []

def setup():
    global bg, castle
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Burg-Verteidiger")
    bg = loadImage("bg.png")
    castle = Castle("castle_100.png") 
    frameRate(FPS)

def draw():
    global bullets
    # background(24, 164, 86)  # Sattes Grün
    image(bg, 0, 0)
    castle.show()
    for bullet in bullets:
        bullet.update()
        bullet.show()
    for i in range(len(bullets) - 1, 0, -1):
        if bullet.delete:
            bullets.pop(i)
    # print(len(bullets))
            
def mousePressed():
    if not castle.fired:
        castle.fired = True
        mouse_pos = PVector(mouseX, mouseY)
        x_dist = mouse_pos.x - castle.x
        y_dist = -(mouse_pos.y - castle.mid_y)
        angle = math.atan2(x_dist, y_dist)
        bullets.append(Bullet(castle.x, castle.mid_y, angle))
        # print(castle.x, castle.mid_y)
        # print("Fire!")

def mouseReleased():
    castle.fired = False
    # print("Press Mouse to fire again")
