class BouncingBall(object):

    def __init__(self, x, y, dia, col):
        self.location = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.d = dia
        self.col = col
        self.gravity = 0.1
        self.dx = 2
        
    def move(self):
        
        # self.location.x += self.dx
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
