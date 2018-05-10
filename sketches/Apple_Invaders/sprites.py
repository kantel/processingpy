tw = 32
th = 32
tileSize = 32

right = 0
up    = 1
left  = 2
down  = 3
standright = 5
standleft = 6

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
        self.imRight = loadImage("gripe_stand_right.png")
        self.imLeft = loadImage("gripe_stand_left.png")
    
    def move(self):
        if self.dir == right:
            self.im = self.imRight
            self.dx = 1
            # self.x += self.dx
        elif self.dir == left:
            self.im = self.imLeft
            self.dx = -1
            # self.x += self.dx
        else:
            self.dx = 0
        self.x += self.dx
    
    def display(self):
        image(self.im, self.x, self.y)
        
