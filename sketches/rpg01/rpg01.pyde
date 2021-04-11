from player import Player
from enemy import Enemy

WIDTH = 800
HEIGHT = 600
vel = 2

def setup():
    global enemy, player
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Flucht & Verfolgung")
    player = Player()
    enemy = Enemy()

def draw():
    global enemy, player
    background(107, 142, 35)
    player.update()
    player.display()
    
    enemy.chase(player.pos)
    enemy.update()
    enemy.display()

def keyPressed():
    global player
    if key == CODED:
        if keyCode == UP:
            player.speed.y -= vel
        elif keyCode == DOWN:
            player.speed.y += vel
        elif keyCode == LEFT:
            player.speed.x -= vel
        elif keyCode == RIGHT:
            player.speed.x += vel
            
def keyReleased():
    global player
    if key == CODED:
        if keyCode == UP or keyCode == DOWN:
            player.speed.y = 0
        elif keyCode == LEFT or keyCode == RIGHT:
            player.speed.x = 0
