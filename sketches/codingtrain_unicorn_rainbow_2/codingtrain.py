class CodingTrain:
    
    def __init__(self, x):
        self.im = loadImage("train.png")
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
