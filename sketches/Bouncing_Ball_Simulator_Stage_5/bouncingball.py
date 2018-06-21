import random as r

class BouncingBall(object):

    def __init__(self):
        self.x = r.randint(20, width - 20)
        self.y = r.randint(20, 200)
        self.location = PVector(self.x, self.y)
        self.velocity = PVector(0, 0)
        self.d = r.randint(15, 30)
        a = 200
        colors = [color(230, 96, 55, a), color(17, 42, 106, a),
                  color(183, 116, 64, a), color(212, 251, 69, a),
                  color(252, 75, 200, a), color(159, 53, 233, a),
                  color(57, 218, 56, a), color(67, 253, 133, a),
                  color(78, 148, 42, a), color(67, 254, 211, a),
                  color(74, 143, 186, a), color(52, 99, 234, a)] 
        self.col = r.choice(colors)
        self.gravity = 0.1
        self.dx = r.randint(-3, 3)
        
    def move(self):
        
        self.velocity.y += self.gravity
        self.location.add(self.velocity)
        self.location.x += self.dx
        
        # check borders
        if self.location.y >= height:
            self.velocity.y *= -1
            self.location.y = height
            
        if self.location.x >= width:
            self.location.x = width - self.d
            self.dx *= -1
        
        if (self.location.x <= 0):
            self.location.x = 0
            self.dx *= -1


    def display(self):
        fill(self.col)
        ellipse(self.location.x, self.location.y, self.d, self.d)
    
class BouncingBox(BouncingBall):
        
    def __init__(self):
        super(BouncingBox, self).__init__()
        self.d = r.randint(10, 25)
        
            
    def display(self):
        fill(self.col)
        rectMode(CENTER)
        rect(self.location.x, self.location.y, self.d, self.d)
