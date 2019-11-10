class Enemy(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 64
    
    def update(self):
        pass
    
    def show(self):
        strokeWeight(1)
        fill("#c666e6")
        ellipse(self.x, self.y, self.r*2, self.r*2) 
