class CodingTrain:
    
    def __init__(self, x):
        self.im = loadImage("train.png")
        self.d = 90 # Durchmesser
        self.pos = PVector(width + x, random(height - 100))
        self.speed = 5
        self.reset = False

    def update(self):
        self.pos.x -= self.speed
        if self.pos.x < -100:
            self.reset = True
            self.pos = PVector(width + 200, random(height - 100))
    
    def show(self):
        image(self.im, self.pos.x, self.pos.y)
        self.reset = False
    
    def rect_collision(self, other):
        distanceX = (self.pos.x + self.d/2) - (other.x + other.d/2)
        distanceY = (self.pos.y + self.d/2) - (other.y + other.d/2)
        halfW = self.d/2 + other.d/2
        halfH = self.d/2 + other.d/2
        if (abs(distanceX) < halfW):
            if (abs(distanceY) < halfH):
                return True
        return False
        
