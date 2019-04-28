# Side Scroller 1
from backgrounds import Hill, Cloud
from sprites import Alien

FPS = 60

clouds = []
bighills = []
smallhills = []
sprites = []

def setup():
    size(800, 450)
    this.surface.setTitle("Side Scroller 1")
    clouds.append(Cloud(400, -1))
    for i in range(3):
        bighills.append(Hill(i*400, 200, -2, "#63e06b"))
    for i in range(6):
        smallhills.append(Hill(i*200, 100, -3, "#217424"))
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
    # Sprites (erst einmal nur das rosa Alien)
    for sprite in sprites:
        sprite.update()
        sprite.show()
