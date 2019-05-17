# Side Scroller 2
from backgrounds import Hill, Cloud
from sprites import Alien, Obstacle

FPS = 60

clouds = []
bighills = []
smallhills = []
sprites = []
obstacles = []

def setup():
    size(800, 450)
    this.surface.setTitle("Side Scroller 2: Jump, Ally, jump!")
    clouds.append(Cloud(400, -1))
    for i in range(3):
        bighills.append(Hill(i*400, 200, -2, "#63e06b"))
    for i in range(6):
        smallhills.append(Hill(i*200, 100, -3, "#217424"))
    obstacles.append(Obstacle(width + 150, 330, "spikes"))
    obstacles.append(Obstacle(width + 650, 330, "spikesBottomAlt"))
    obstacles.append(Obstacle(width + 750, 330, "spikesBottom"))
    obstacles.append(Obstacle(width + 1190, 330, "fence"))
    obstacles.append(Obstacle(width + 1250, 330, "fenceBroken"))
    obstacles.append(Obstacle(width + 1310, 330, "fence"))
    sprites.append(Alien(66, 320))
    frameRate(FPS)
    noStroke()

def draw():
    background(64, 176, 226)
    # Wolke(n) im Hintergrund
    for cloud in clouds:
        cloud.update()
        cloud.show()
    # Große Hügel im Hintergrund
    for hill in bighills:
        hill.update()
        hill.show()
    # Kleine Hügel im Vordergrund         
    for hill in smallhills:
        hill.update()
        hill.show()
    # Erdboden    
    fill("#ffd05e")
    rect(0, 400, width, 50)
    # Obstacles
    for obstacle in obstacles:
        obstacle.update()
        obstacle.show()
    # Sprites (erst einmal nur das rosa Alien)
    for sprite in sprites:
        sprite.update()
        sprite.show()
    # saveFrame("frames/####.png")

def keyPressed():
    alien = sprites[0]
    if key == CODED:
        if keyCode == UP and alien.status == "walking":
            alien.vely = -5
            alien.status = "jumping"
    
