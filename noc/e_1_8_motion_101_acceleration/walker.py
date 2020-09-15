class Walker:
    
    def __init__(self):
        self.location = PVector(width/2, height/2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(-0.001, 0.1)
        self.topspeed = 10
        self.d = 20
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.location.add(self.velocity)
    
    def checkEdges(self):
        if (self.location.x > width):
            self.location.x = 0
        elif (self.location.x < 0):
            self.location.x = width
        
        if (self.location.y > height):
            self.location.y = 0
        elif (self.location.y < 0):
            self.location.y = height
    
    def display(self):
        stroke(0)
        fill(240, 80, 37)
        circle(self.location.x, self.location.y, self.d)
