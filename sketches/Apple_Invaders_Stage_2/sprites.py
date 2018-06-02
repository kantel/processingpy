tw = 32
import random as r

th = 32
tileSize = 32

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
        self.dx = 10
        self.dy = 0
        self.score = 0
        self.dir = "right"
        # self.newdir = "right"
        self.state = "standing"
        self.walkR = []
        self.walkL = []
    
    def loadPics(self):
        self.standR = loadImage("gripe_stand_right.png")
        self.standL = loadImage("gripe_stand_left.png")
        self.falling = loadImage("grfalling.png")
        for i in range(8):
            imageName = "gr" + str(i) + ".png"
            self.walkR.append(loadImage(imageName))
        for i in range(8):
            imageName = "gl" + str(i) + ".png"
            self.walkL.append(loadImage(imageName))
            
    def checkWall(self, wall):
        if wall.state == "hidden":
            if (self.x >= wall.x - 3 and
                    (self.x + 32 <= wall.x + 32 + 3)):
                return False
    
    def move(self):
        if self.dir == "right":
            if self.state == "walking":
                self.im = self.walkR[frameCount % 8]
                self.dx = 3
            elif self.state == "standing":
                self.im = self.standR
                self.dx = 0
            elif self.state == "falling":
                self.im = self.falling
                self.dx = 0
                self.dy = 5
        elif self.dir == "left":
            if self.state == "walking":
                self.im = self.walkL[frameCount % 8]
                self.dx = -3
            elif self.state == "standing":
                self.im = self.standL
                self.dx = 0
            elif self.state == "falling":
                self.im = self.falling
                self.dx = 0
                self.dy = 5
        else:
            self.dx = 0
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0:
            self.x = 0
        if self.x >= 640 - tw:
            self.x = 640 - tw
    
    def display(self):
        image(self.im, self.x, self.y)
        

class Apple(Sprite):
    
    def __init__(self, xPos, yPos):
        super(Apple, self).__init__(xPos, yPos)
        if r.randint(0, 100) < 5:
            self.state = "green"
        else:
            self.state = "red"
        self.speed = 1
    
    def loadPics(self):
        self.imRed = loadImage("applered.png")
        self.imGreen = loadImage("applegreen.png")
    
    def move(self):
        self.y += self.speed
        if self.y >= height + 32:
            self.reset()

    def reset(self):
        self.x = r.randint(32, width-32)
        self.y = r.randint(-480, -48)
        if r.randint(0, 100) < 10:
            self.state = "green"
        else:
            self.state = "red"
                            
    def display(self):
        if self.state == "green":
            self.im = self.imGreen
        elif self.state == "red":
            self.im = self.imRed
        image(self.im, self.x, self.y)


class Block(Sprite):
    
    def __init__(self, xPos, yPos):
        super(Block, self).__init__(xPos, yPos)
        self.state = "visible"
    
    def loadPics(self):
        self.im = loadImage("block.png")
    
    def display(self):
        if self.state == "visible":
            image(self.im, self.x, self.y)
        
