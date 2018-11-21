class Mover(object):
    
    def __init__(self):
        self.location = PVector(width/2, height/2)
        self.velocity = PVector(0, 0)
        self.topspeed = 10
        self.r = 15
    
    def update(self):
        self.acceleration = PVector.random2D()
        # self.acceleration.mult(0.5)
        self.acceleration.mult(random(2))
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
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
 
        
        
