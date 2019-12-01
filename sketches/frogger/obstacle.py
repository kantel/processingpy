from rectangle import Rectangle

class Obstacle(Rectangle):
    
    def __init__(self, x, y, w, h, s, i):
        super(Rectangle, self).__init__(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.speed = s
        self.img = loadImage(i)
    
    def update(self):
        self.x += self.speed
        if (self.speed > 0 and self.x > width + GRID):
            self.x = -self.w - GRID
        elif (self.speed < 0 and self.x < -self.w - GRID):
            self.x = width + GRID
    
    def show(self):
        image(self.img, self.x, self.y)
