class Walker:
    
    def __init__(self):
        self.location = PVector(100, 100)
        self.velocity = PVector(2.5, 5)
        self.d = 20
    
    def update(self):
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
