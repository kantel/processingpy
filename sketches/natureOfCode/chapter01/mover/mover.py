class Mover(object):
    
    def __init__(self):
        self.location = PVector(random(width), random(height))
        self.velocity = PVector(random(-5, 5), random(-5, 5))
        self.r = 15
    
    def update(self):
        self.location.add(self.velocity)
    
    def display(self):
        stroke(0)
        fill(255, 100, 255)
        ellipse(self.location.x, self.location.y, 2*self.r, 2*self.r)
    
    def checkBoundaries(self):
        if (self.location.x > width + self.r):
            self.location.x = -self.r
        elif (self.location.x < -self.r):
            self.location.x = width + self.r
        
        if (self.location.y > height + self.r):
            self.location.y = -self.r
        elif (self.location.y < -self.r):
            self.location.y = height + self.r
 
        
        
