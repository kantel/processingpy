class Fish():
    
    def __init__(self):
        self.x = 50
        self.y = 240
        self.r = 32
        
        self.gravity = 0.6
        self.lift = -12
        self.velocity = 0
        
    def loadPic(self):
        self.pic = loadImage("fisch2.png")
        
    def up(self):
        self.velocity += self.lift
        
    def display(self):
        image(self.pic, self.x, self.y)
    
    def update(self):
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity
        if (self.y >= height - self.r):
            self.y = height - self.r
            self.velocity = 0
        elif (self.y <= 0):
            self.y = 0
            self.velocity = 0
            
        
