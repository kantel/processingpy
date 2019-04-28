# coding=utf-8

class Sprite(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def update(self):
        pass
    
    def show(self):
        pass

class Alien(Sprite):
    
    def __init__(self, x, y):
        Sprite.__init__(self, x, y)
        self.status = "walking"
        self.im1 = loadImage("alienwalk1.png")
        self.im2 = loadImage("alienwalk2.png")
        self.count = 0
        
    def show(self):
        if self.status == "walking":
            self.count += 1
            if self.count > 15:
                self.count = 0
            if self.count < 8:
                image(self.im1, self.x, self.y)
            else:
                image(self.im2, self.x, self.y)
        
