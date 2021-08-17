from random import randint

WIDTH = 640
HEIGHT = 480
N_BUBBLES = 25
N_ENEMIES = 5

bubbles = []
enemies = []

class Crab():
    
    def __init__(self):
        self.pos = PVector(width/2 - 34, height - 80)
        self.img = loadImage("crab.png")
        self.w = 68
        self.speed = PVector(0, 0)
        self.score = 0
        self.vel = 0.5
        self.r = 25
    
    def update(self):
        self.pos.x += self.speed.x
        if self.pos.x >= width - self.w:
            self.pos.x = width - self.w
            self.speed.x = 0
        if self.pos.x <= 0:
            self.pos.x = 0
            self.speed.x = 0

    def display(self):
        image(self.img, self.pos.x, self.pos.y)
    
    def check_collision(self, other):
        distance = dist(self.pos.x, self.pos.y, other.pos.x, other.pos.y)
        if distance < self.r + other.r:
            other.reset()
            self.score += 1
            print(self.score)

class Bubble():
    
    def __init__(self):
        self.pos = PVector(randint(0, width - 30), randint(-640, -30))
        self.img = loadImage("bubble.png")
        self.r = 15
        self.speed = 2
    
    def update(self):
        self.pos.y += self.speed
        if self.pos.y >= height:
            self.reset()
    
    def reset(self):
        self.pos.x = randint(0, width - 30)
        self.pos.y = randint(-640, -30)
        
    
    def display(self):
        image(self.img, self.pos.x, self.pos.y)

class Enemy():
    
    def __init__(self):
        self.pos = PVector(randint(0, width - 30), randint(-640, -30))
        self.img = loadImage("enemy.png")
        self.r = 15
        self.speed = 2
    
    def update(self):
        self.pos.y += self.speed
        if self.pos.y >= height:
            self.reset()
    
    def reset(self):
        self.pos.x = randint(0, width - 30)
        self.pos.y = randint(-640, -30)
        
    
    def display(self):
        image(self.img, self.pos.x, self.pos.y)


def setup():
    global bg, crab
    size(WIDTH, HEIGHT)
    this.surface.setTitle(u"Jörgs kleines Krabbenspiel")
    bg = loadImage("bg.png")
    crab = Crab()
    for _ in range(N_BUBBLES):
        bubbles.append(Bubble())
    for _ in range(N_ENEMIES):
        enemies.append(Enemy())
    
def draw():
    background(49, 197, 244)
    image(bg, 0, 0)
    for bubble in bubbles:
        bubble.update()
        crab.check_collision(bubble)
        bubble.display()
    for enemy in enemies:
        enemy.update()
        enemy.display()
    crab.update()
    crab.display()
    
    
def keyPressed():
    # global crab
    if key == CODED:
        if keyCode == LEFT:
            crab.speed.x -= crab.vel
        elif keyCode == RIGHT:
            crab.speed.x += crab.vel

def keyReleased():
    if key == CODED:
        if keyCode == LEFT or keyCode == RIGHT:
            crab.speed.x = 0
            
    
