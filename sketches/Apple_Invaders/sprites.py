tw = 32
th = 32
tileSize = 32

right = 0
up    = 1
left  = 2
down  = 3
standingright = 4
standingleft = 5

class Sprite(object):
    
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
    
    def checkCollision(self, otherSprite):
        if (self.x < otherSprite.x + tw and otherSprite.x < self.x + tw
            and self.y < otherSprite.y + th and otherSprite.y < self.y + th):
            return True
        else:
            return False

class Actor(Sprite):
    
    def __init__(self, xPos, yPos):
        super(Actor, self).__init__(xPos, yPos)
        self.dx = 3
        self.dir = right
    
    def loadPics(self):
        self.standR = loadImage("gripe_stand_right.png")
        self.standL = loadImage("gripe_stand_left.png")
        self.walkR0 = loadImage("gr0.png")
        self.walkR1 = loadImage("gr1.png")
        self.walkR2 = loadImage("gr2.png")
        self.walkR3 = loadImage("gr3.png")
        self.walkR4 = loadImage("gr4.png")
        self.walkR5 = loadImage("gr5.png")
        self.walkR6 = loadImage("gr6.png")
        self.walkR7 = loadImage("gr7.png")
        self.walkL0 = loadImage("gl0.png")
        self.walkL1 = loadImage("gl1.png")
        self.walkL2 = loadImage("gl2.png")
        self.walkL3 = loadImage("gl3.png")
        self.walkL4 = loadImage("gl4.png")
        self.walkL5 = loadImage("gl5.png")
        self.walkL6 = loadImage("gl6.png")
        self.walkL7 = loadImage("gl7.png")
    
    def move(self):
        if self.dir == right:
            self.im = self.walkR0
            self.dx = 1
        elif self.dir == left:
            self.im = self.walkL0
            self.dx = -1
        else:
            self.dx = 0
        self.x += self.dx

        if self.x <= 0:
            self.x = 0
        if self.x >= 640 - tw:
            self.x = 640 - tw
    
    def display(self):
        image(self.im, self.x, self.y)
        
