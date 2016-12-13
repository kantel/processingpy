tw = 32
th = 32
tileSize = 32

class Sprite(object):

    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
        self.dir = 1
        self.dx = 0
        self.dy = 0
    
    def checkCollision(self, otherSprite):
        if (self.x < otherSprite.x + tw and otherSprite.x < self.x + tw
            and self.y < otherSprite.y + th and otherSprite.y < self.y + th):
            return True
        else:
            return False
class Hero(Sprite):

    def loadPics(self):
        self.mnv1rt1 = loadImage("mnv1rt1.gif")
        self.mnv1rt2 = loadImage("mnv1rt2.gif")
        self.mnv1fr1 = loadImage("mnv1fr1.gif")
        self.mnv1fr2 = loadImage("mnv1fr2.gif")
        self.mnv1lf1 = loadImage("mnv1lf1.gif")
        self.mnv1lf2 = loadImage("mnv1lf2.gif")
        self.mnv1bk1 = loadImage("mnv1bk1.gif")
        self.mnv1bk2 = loadImage("mnv1bk2.gif")
    
    def move(self):
        if self.dir == 0:
            if self.x >= width - tileSize:
                self.x = width - tileSize
                self.image1 = self.mnv1rt2
                self.image2 = self.mnv1rt2
            else:
                self.x += self.dx
                self.image1 = self.mnv1rt1
                self.image2 = self.mnv1rt2
        elif self.dir == 1:
            if self.y >= height - tileSize:
                self.y = height - tileSize
                self.image1 = self.mnv1fr2
                self.image2 = self.mnv1fr2
            else:
                self.y += self.dy
                self.image1 = self.mnv1fr1
                self.image2 = self.mnv1fr2
        elif self.dir == 2:
            if self.x <= 0:
                self.x = 0
                self.image1 = self.mnv1lf2
                self.image2 = self.mnv1lf2
            else:
                self.x -= self.dx
                self.image1 = self.mnv1lf1
                self.image2 = self.mnv1lf2
        elif self.dir == 3:
            if self.y <= 0:
                self.y = 0
                self.image1 = self.mnv1bk2
                self.image2 = self.mnv1bk2
            else:
                self.y -= self.dy
                self.image1 = self.mnv1bk1
                self.image2 = self.mnv1bk2
                
    def display(self):
        if frameCount % 8 >= 4:
            image(self.image1, self.x, self.y)
        else:
            image(self.image2, self.x, self.y)

class Obstacle(Sprite):
    
    def loadPics(self):
        self.pic = loadImage("wall.png")
        
    def display(self):
        image(self.pic, self.x, self.y)
