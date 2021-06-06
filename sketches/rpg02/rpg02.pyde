from player import Player
from enemy import Enemy
from settings import *

WIDTH = 800
HEIGHT = 600

def setup():
    global enemy, player
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Flucht & Verfolgung v02")
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
    if (abs(enemy.pos.x - player.pos.x) <= epsilon and 
        abs(enemy.pos.y - player.pos.y) <= epsilon): 
        print("Player lost!")
        noLoop() 
        
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
