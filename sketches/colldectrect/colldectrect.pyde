from enemies import Enemy
from player import Player

def setup():
    global enemy, player
    size(420, 420)
    this.surface.setTitle("Rectangle Collision Detection")
    enemy = Enemy(width/2 - 64, height/2 - 32)
    player = Player(20, 20)

def draw():
    global enemy, player
    background("#95ee0f5")
    if rect_collision(enemy, player):
        background("#817ac6")
    else:
        background("#95ee0f5")
    enemy.show()
    player.update()
    player.show()

def rect_collision(r1, r2):
    distanceX = (r1.x + r1.w/2) - (r2.x + r2.w/2)
    distanceY = (r1.y + r1.h/2) - (r2.y + r2.h/2)
    halfW = r1.w/2 + r2.w/2
    halfH = r1.h/2 + r2.h/2
    if (abs(distanceX) < halfW):
        if (abs(distanceY) < halfH):
            return True
    return False
