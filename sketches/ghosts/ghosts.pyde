from random import randint
from disk import Disk

WIDTH = 640
HEIGHT = 480
BORDER = 50
N_DISKS = 10

def setup():
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Ghost Busters")
    ghost_factory()
    
def draw():
    global disks
    background(132, 144, 163)
    for disk in disks:
        disk.update()
        disk.show()

def ghost_factory():
    global disks
    disks = []
    for _ in range(N_DISKS):
        x_pos = randint(BORDER, width - BORDER)
        y_pos = randint(BORDER, height - BORDER)
        x_dir = randint(-8, 8)
        y_dir = randint(-8, 8)
        radius = randint(10, 30)
        clr = color(randint(20, 250), randint(20, 250), randint(20, 250), 180)
        disks.append(Disk(x_pos, y_pos, x_dir, y_dir, radius, clr))
        
    
