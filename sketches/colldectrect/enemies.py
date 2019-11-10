class Enemy(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 128
        self.h = 64
    
    def update(self):
        pass
    
    def show(self):
        strokeWeight(1)
        fill("#c666e6")
        rect(self.x, self.y, self.w, self.h) 
