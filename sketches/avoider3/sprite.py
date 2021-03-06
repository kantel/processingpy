from random import randint

tw = th = 36

class Sprite(object):
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY

    def checkCollision(self, otherSprite):
        if (self.x < otherSprite.x + tw and otherSprite.x < self.x + tw
            and self.y < otherSprite.y + th and otherSprite.y < self.y + th):
            return True
        else:
            return False


class Skull(Sprite):

    def __init__(self, posX, posY):
        super(Skull, self).__init__(posX, posY)
        self.score = 0
        self.health = 0
            
    def loadPics(self):
        self.im1 = loadImage("skull.png")
        
    def move(self):
        self.x = mouseX
        if self.x <= 0:
            self.x = 0
        elif self.x >= width-tw:
            self.x = width - tw
            
    def display(self):
        image(self.im1, self.x, self.y)

class Smiley(Sprite):
    
    def __init__(self, posX, posY):
        super(Smiley, self).__init__(posX, posY)
        self.outside = False

    def loadPics(self):
        self.im0 = loadImage("smiley0.png")
        self.im1 = loadImage("smiley1.png")
        self.im2 = loadImage("smiley4.png")
        
    def move(self):
        self.outside = False
        self.y += self.dy
        if self.y >= height:
            self.outside = True
            self.y = -randint(50, 250)
            self.x = randint(0, width-tw)
            self.dy = randint(4, 10)
        
    def display(self):
        if (self.y > -30) and (self.y <= 250):
            image(self.im0, self.x, self.y)
        elif (self.y > 250) and (self.y <= 320):
            image(self.im1, self.x, self.y)
        elif (self.y > 320):
            image(self.im2, self.x, self.y)
    
    def reset(self, posX, posY):
        self.x = posX
        self.y = posY
            
class Star(object):
    
    def __init__(self, posX, posY, dia, speed):
        self.x = posX
        self.y = posY
        self.r = dia
        self.dy = speed
        self.a = 255 # Transparency
    
    def move(self):
        self.outside = False
        self.y += self.dy
        if self.y >= height:
            self.outside = True
            self.y = -2*self.r
            self.x = randint(0, width - 2*self.r)
    
    def display(self):
        fill(255, 255, 255, self.a)
        noStroke()
        ellipse(self.x, self.y, self.r, self.r)