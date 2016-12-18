tw = 32
th = 44


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

class Pingus(Sprite):

    def loadPics(self):
        self.pingrt1 = loadImage("pingrt1.gif")
        self.pingrt2 = loadImage("pingrt2.gif")
        self.pingrt3 = loadImage("pingrt3.gif")
        self.pingrt4 = loadImage("pingrt4.gif")
        self.pingrt5 = loadImage("pingrt5.gif")
        self.pingrt6 = loadImage("pingrt6.gif")
        self.pingrt7 = loadImage("pingrt7.gif")
        self.pingrt8 = loadImage("pingrt8.gif")
        self.pinglft1 = loadImage("pinglft1.gif")
        self.pinglft2 = loadImage("pinglft2.gif")
        self.pinglft3 = loadImage("pinglft3.gif")
        self.pinglft4 = loadImage("pinglft4.gif")
        self.pinglft5 = loadImage("pinglft5.gif")
        self.pinglft6 = loadImage("pinglft6.gif")
        self.pinglft7 = loadImage("pinglft7.gif")
        self.pinglft8 = loadImage("pinglft8.gif")
        
    def move(self):
        if self.dir == 1:
            if self.x >= width:
                self.dir = -1
            else:
                self.x -= self.dx
                self.image1 = self.pingrt1
                self.image2 = self.pingrt2
        else:
            if self.x <= 0:
                self.dir = 1
            else:
                self.x += self.dx
                self.image1 = self.pinglft1
                self.image2 = self.pinglft2
                
    def display(self):
        if frameCount % 8 >= 4:
            image(self.image1, self.x, self.y)
        else:
            image(self.image2, self.x, self.y)
            
