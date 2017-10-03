# coding=utf-8

class Paddle(object):

    def __init__(self):
        self.w = 120
        self.h = 15
        self.pos = PVector(width/2.0 - self.w/2.0, height - 40)
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

class Ball(object):
    
    def __init__(self):
        self.r = 10
        self.vel = PVector(1, 1)*4
        self.dir = PVector(1, 1)
        self.pos = PVector(width/2, height/2)
    
    def update(self):
        self.pos.x += self.vel.x*self.dir.x
        self.pos.y += self.vel.y*self.dir.y
    
    def display(self):
        fill("#ffff64")
        noStroke()
        ellipse(self.pos.x, self.pos.y, self.r*2, self.r*2)
    
    def checkEdges(self):
        # rechter Rand
        if (self.pos.x > width - self.r and self.dir.x > 0):
            self.dir.x *= -1
        # linker Rand
        if (self.pos.x < self.r and self.dir.x < 0):
            self.dir.x *= -1
        # top
        if (self.pos.y < self.r and self.dir.y < 0):
            self.dir.y *= -1
        # bottom (wird später gelöscht)
        if (self.pos.y > height - self.r and self.dir.y > 0):
            self.dir.y *= -1
        
    def meets(self, paddle):
        if (self.pos.y < paddle.pos.y and
            self.pos.y > paddle.pos.y - self.r and
            self.pos.x > paddle.pos.x - self.r and
            self.pos.x < paddle.pos.x + paddle.w + self.r):
            return True
        else:
            return False


class Brick(object):
    
    COLORS = {1: "#64ff96", 2: "#ff6496", 3: "#9664ff"}
    
    def __init__(self, x, y, hits):
        self.w = 75
        self.h = 20
        self.pos = PVector(x, y)
        self.hits = hits
        self.col = Brick.COLORS[hits]
    
    def display(self):
        fill(self.col)
        stroke("#ffffff")
        strokeWeight(2)
        rect(self.pos.x, self.pos.y, self.w, self.h)