class Spaceship():
    
    def __init__(self, pic, posX, posY):
        self.pic = pic
        self.x = posX
        self.y = posY
        self.dx = 0
        self.dy = 0
        
    def loadPic(self):
        self.img = loadImage(self.pic)
    
    def move(self):
        self.x += self.dx
        if self.x >= width + 120:
            self.x = -120
            self.y = random(height-120)
        elif self.x < -120:
            self.x = width + 120
            self.y = random(height-120)
    
    def display(self):
        image(self.img, self.x, self.y)

class Octopussy(Spaceship):
    
    def move(self):
        self.y += self.dy
        if self.dy >= 5:
            self.dy = 5
        elif self.dy <= -5:
            self.dy = -5
        if self.y < 0:
            self.y = 0
            self.dy = 0
        if self.y > height - 120:
            self.y = height - 120
            self.dy = 0