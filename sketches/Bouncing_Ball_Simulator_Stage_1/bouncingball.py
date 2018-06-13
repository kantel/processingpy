class BouncingBall(object):
    
    def __init__(self, x, y, dia, col):
        self.x = x
        self.y = y
        self.diameter = dia
        self.col = col
        self.dy = 0
        self.gravity = 0.1
        
    def move(self):
        self.dy += self.gravity
        self.y += self.dy
        
        # check borders
        if self.y >= height:
            self.dy *= -1
            self.y = height
    
    def display(self):
        fill(self.col)
        ellipse(self.x, self.y, self.diameter, self.diameter)
