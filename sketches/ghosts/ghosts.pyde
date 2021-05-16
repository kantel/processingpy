from random import randint
from disk import Disk

WIDTH = 640
HEIGHT = 480
BORDER = 50
N_DISKS = 30
SPEED = 4
MIN_R = 10
MAX_R = 25

FPS = 60

def setup():
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Bubble Busters")
    bubble_factory()
    frameRate(FPS)
    
def draw():
    global disks
    background(132, 144, 163)
    for disk in disks:
        disk.update()
        for other_disk in disks:
            disk.circle_collision(other_disk)
        disk.show()
    # if frameCount <= 3600:
    #     saveFrame("pics/####.png")
    # else:
    #     print("I did it Babe")
    #     noLoop()

def bubble_factory():
    global disks
    disks = []
    for _ in range(N_DISKS):
        x_pos = randint(BORDER, width - BORDER)
        y_pos = randint(BORDER, height - BORDER)
        x_dir = randint(-SPEED, SPEED)
        if x_dir == 0:
            x_dir = 1
        y_dir = randint(-SPEED, SPEED)
        if y_dir == 0:
            y_dir = -1
        radius = randint(MIN_R, MAX_R)
        clr = color(randint(20, 250), randint(20, 250), randint(20, 250), 180)
        disks.append(Disk(x_pos, y_pos, x_dir, y_dir, radius, clr))
  
      
