from player import Player
from enemy import Enemy
from settings import *
enemies = []

def setup():
    global enemy, player
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Flucht & Verfolgung v02")
    my_font = createFont("American Typewriter", 30)
    textFont(my_font)
    player = Player()
    for _ in range(no_enemies):
        enemies.append(Enemy())
    
def draw():
    global enemy, player
    background(107, 142, 35)
    for enemy in enemies:
        enemy.chase(player.pos)
        enemy.update()
        enemy.display()
    player.update()
    player.display()
    if player.check_collision(enemy):
        fill(200, 0, 0)
        text(u"Du hast verloren!", 20, 40)
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
