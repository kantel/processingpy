class Player(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 32
        self.h = 32
    
    def update(self):
        self.x = mouseX
        self.y = mouseY
    
    def show(self):
        strokeWeight(1)
        fill("#9757a5")
        rect(self.x, self.y, self.w, self.h)
