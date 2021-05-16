from random import randint

MIN_R = 10
MAX_R = 25

class Disk():
    
    def __init__(self, _x, _y, _ax, _ay, _r, _clr):
        self.pos = PVector(_x, _y)
        self.dir = PVector(_ax, _ay)
        self.radius = _r
        self.clr = _clr
    
    def update(self):
        self.pos.add(self.dir)
        if (self.pos.x - 2*self.radius <= 0):
            self.pos.x = 2*self.radius
            self.dir.x *= -1
        if (self.pos.x + 2*self.radius >= width):
             self.pos.x = width - 2*self.radius
             self.dir.x *= -1
        if (self.pos.y - 2*self.radius <= 0):
            self.pos.y = 2*self.radius
            self.dir.y *= -1
        if (self.pos.y + 2*self.radius >= height):
             self.pos.y = height - 2*self.radius
             self.dir.y *= -1
    
    def show(self):
        fill(self.clr)
        circle(self.pos.x, self.pos.y, self.radius*2)
    
    def circle_collision(self, other):
        if other != self:
            distance = abs(dist(self.pos.x, self.pos.y, other.pos.x, other.pos.y))
            if distance <= self.radius + other.radius:
                self.reset()
                other.reset()
       
    def reset(self):
        self.pos = PVector(randint(2*self.radius, width - 2*self.radius),
                           randint(2*self.radius, height - 2*self.radius))
        self.dir *= -1
        self.radius = randint(MIN_R, MAX_R)
        self.clr = color(randint(20, 250), randint(20, 250), randint(20, 250), 180)
