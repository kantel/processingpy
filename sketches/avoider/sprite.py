from random import randint

tw = th = 36

class Sprite():
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
        self.dx = 0
        self.dy = 0

class Skull(Sprite):
    
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
    
    def loadPics(self):
        self.im1 = loadImage("smiley1.png")
        
    def move(self):
        self.y += self.dy
        if self.y >= height:
            self.y = -randint(50, 250)
            self.x = randint(0, width-tw)
        
    def display(self):
        image(self.im1, self.x, self.y)
