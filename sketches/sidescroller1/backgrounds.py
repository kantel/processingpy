# coding=utf-8

class Hill(object):
    
    def __init__(self, x, r, s, c):
        self.xpos = x
        self.radius = r
        self.step = s
        self.col = c
    
    def update(self):
        self.xpos += self.step
        if self.xpos <= -self.radius:
            self.xpos = width + self.radius
    
    def show(self):
        fill(self.col)
        circle(self.xpos, 400, 2*self.radius)

class Cloud(object):
    
    def __init__(self, x, s):
        self.xpos = x
        self.step = s
    
    def update(self):
        self.xpos += self.step
        if self.xpos <= -200:
            self.xpos = width + 200
    
    def show(self):
        fill("#ffffff")
        circle(self.xpos, 150, 100)
        circle(self.xpos, 200, 100)
        circle(self.xpos - 50, 200, 100)
        circle(self.xpos + 50, 200, 100)
        
