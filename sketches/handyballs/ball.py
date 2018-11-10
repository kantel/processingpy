import random as r

class Ball(object):

    def __init__(self, renderer):
        self.h = renderer
        self.r = r.randint(20, 40)
        self.vel = PVector(1, 1)*r.uniform(1.0, 4.0)
        self.dir = PVector(-1.5, 1.5)
        self.pos = PVector(r.randint(80, width - 80), r.randint(80, height - 80))
        self.red = (r.randint(100, 255))
        self.green = (r.randint(0, 150))
        self.blue = (r.randint(0, 255))

    def update(self):
        self.pos.x += self.vel.x*self.dir.x
        self.pos.y += self.vel.y*self.dir.y

    def display(self):
        fill(self.red, self.green, self.blue)
        # self.h.noStroke()
        self.h.ellipse(self.pos.x, self.pos.y, self.r*2, self.r*2)

    def checkEdges(self):
        # rechter Rand
        if (self.pos.x > width - 40 - self.r and self.dir.x > 0):
            self.dir.x *= -1
        # linker Rand
        if (self.pos.x < self.r + 40 and self.dir.x < 0):
            self.dir.x *= -1
        # top
        if (self.pos.y < self.r + 40 and self.dir.y < 0):
            self.dir.y *= -1
        # bottom
        if (self.pos.y > height - 40 - self.r and self.dir.y > 0):
            self.dir.y *= -1
