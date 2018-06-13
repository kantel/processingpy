class BouncingBall(object):
    
    
    
    def __init__(self, x, y, dia, col):
        self.location = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.diameter = dia
        self.col = col
        self.gravity = 0.1
        
    def move(self):
        self.velocity.y += self.gravity
        self.location.add(self.velocity)
        
        # check borders
        if self.location.y >= height:
            self.velocity.y *= -1
            self.location.y = height
    
    def display(self):
        fill(self.col)
        ellipse(self.location.x, self.location.y, self.diameter, self.diameter)
