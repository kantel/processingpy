class Player(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 32
    
    def update(self):
        self.x = mouseX
        self.y = mouseY
    
    def show(self):
        strokeWeight(1)
        fill("#9757a5")
        ellipse(self.x, self.y, self.r*2, self.r*2)
