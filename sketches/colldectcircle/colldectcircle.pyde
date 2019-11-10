from enemies import Enemy
from player import Player

def setup():
    global enemy, player
    size(420, 420)
    this.surface.setTitle("Circle Collision Detection")
    enemy = Enemy(width/2, height/2)
    player = Player(20, 20)

def draw():
    global enemy, player
    background("#95ee0f5")
    if circle_collision(enemy, player):
        background("#817ac6")
    else:
        background("#95ee0f5")
    enemy.show()
    player.update()
    player.show()

def circle_collision(c1, c2):
    distance = dist(c1.x, c1.y, c2.x, c2.y)
    if distance < c1.r + c2.r:
        return True
    else:
        return False
