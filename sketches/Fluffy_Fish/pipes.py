class Pipe():
    
    def __init__(self):
        self.top = random(height) - 60
        if self.top < 60:
            self.top = 60
        if self.top > height - 180:
            self.top = height - 180
        self.bottom = height - self.top - 120
        # self.bottom = random(height/2)
        self.x = width
        self.w = 40
        self.speed = 2
        self.hilite = False
    
    def display(self):
        fill(0, 125, 0)
        if self.hilite:
            fill(255, 0, 0)
        rect(self.x, 0, self.w, self.top)
        rect(self.x, height - self.bottom, self.w, self.bottom)
    
    def update(self):
        self.x -= self.speed
    
    def offscreen(self):
        if (self.x < -self.w):
            return True
        else:
            return False
    
    def collidesWith(self, otherObject):
        if (otherObject.y - otherObject.r/2 < self.top) or (otherObject.y + otherObject.r/2 > height - self.bottom):
            if (otherObject.x + otherObject.r/2 > self.x) and (otherObject.x - otherObject.r/2 < self.x + self.w):
                return True
        else:
            return False
        
