# Mein kleines Krabbenspiel, in Processing.py implementiert von Jörg Kantel
# Nach einer Idee von Hauke Fehr in TigerJython: Let's code Python, Bonn (Rheinwerk Verlag) 2019, Seite 247 - 266
# Font: »Gorditas« von Gustave Dipre ®(Google Fonts, Open Font Licence, https://fonts.google.com/specimen/Gorditas)
# Sprites: TigerJython Sprites (https://www.tigerjython.ch/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=sprites.html)

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
            # print(self.score)

class Bubble():
    
    def __init__(self):
        self.pos = PVector(randint(0, width - 30), randint(-640, -30))
        self.img = loadImage("bubble.png")
        self.r = 15
        self.speed = randint(1, 3)
    
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
        self.speed = randint(2, 4)
    
    def update(self):
        self.pos.y += self.speed
        if self.pos.y >= height:
            self.reset()
    
    def reset(self):
        self.pos.x = randint(0, width - 30)
        self.pos.y = randint(-640, -30)
            
    def display(self):
        image(self.img, self.pos.x, self.pos.y)
        
    def check_collision(self, other):
        distance = dist(self.pos.x, self.pos.y, other.pos.x, other.pos.y)
        if distance < self.r + other.r:
            return(True)

def setup():
    global bg, crab, you_lost
    size(WIDTH, HEIGHT)
    this.surface.setTitle(u"Jörgs kleines Krabbenspiel")
    font = createFont("Gorditas-Bold.ttf", 40)
    textFont(font)
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
        if enemy.check_collision(crab):
            textAlign(CENTER)
            fill(250, 0, 0)
            textSize(40)
            text("Game Over", width/2, height/2)
            noLoop()
        enemy.display()
    crab.update()
    crab.display()
    fill(250, 0, 0)
    textAlign(LEFT)
    textSize(30)
    text("Score: " + str(crab.score), 15, 40)
        
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
            
    
