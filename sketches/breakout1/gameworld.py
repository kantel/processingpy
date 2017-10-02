class Paddle(object):

    def __init__(self):
        self.w = 120
        self.h = 15
        self.pos = PVector(width / 2 - self.w / 2, height - 40)
        self.isMovingLeft = False
        self.isMovingRight = False
        self.stepSize = 20

    def display(self):
        fill("#ff9664")
        noStroke()
        rect(self.pos.x, self.pos.y, self.w, self.h)

    def update(self):
        if self.isMovingLeft:
            self.move(-self.stepSize)
        elif self.isMovingRight:
            self.move(self.stepSize)

    def move(self, step):
        self.pos.x += step

    def checkEdges(self):
        if self.pos.x <= 0:
            self.pos.x = 0
        elif self.pos.x + self.w >= width:
            self.pos.x = width - self.w
