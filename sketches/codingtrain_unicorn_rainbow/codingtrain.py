class CodingTrain:
    
    def __init__(self):
        self.im = loadImage("train.png")
        self.pos = PVector(width + 200, random(height - 100))
        self.speed = 5
    
    def update(self):
        self.pos.x -= self.speed
        if self.pos.x < -100:
            self.pos = PVector(width + 200, random(height - 100))
    
    def show(self):
        image(self.im, self.pos.x, self.pos.y)
