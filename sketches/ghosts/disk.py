class Disk():
    
    def __init__(self, ax_p, ay_p, ax_d, ay_d, a_r, a_clr):
        self.pos = PVector(ax_p, ay_p)
        self.dir = PVector(ax_d, ay_d)
        self.radius = a_r
        self.clr = a_clr
    
    def update(self):
        self.pos += self.dir
        if (self.pos.x - self.radius <= 0) or (self.pos.x + self.radius >= width):
            self.dir.x *= -1
            self.pos.x += 2*self.dir.x
        if (self.pos.y - self.radius <= 0) or (self.pos.y + self.radius >= height):
            self.dir.y *= -1
            self.pos.y += 2*self.dir.y
    
    def show(self):
        fill(self.clr)
        circle(self.pos.x, self.pos.y, self.radius)
