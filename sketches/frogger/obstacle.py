from rectangle import Rectangle

GRID = 40

class Obstacle(Rectangle):
    
    def __init__(self, x, y, w, h, s, im):
        super(Rectangle, self).__init__(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.speed = s
        self.img = loadImage(str(im))
    
    def update(self):
        self.x += self.speed
        if (self.speed > 0 and self.x >= width):
            self.x = -self.w
        elif (self.speed < 0 and self.x < -self.w):
            self.x = width
    
    def show(self):
        image(self.img, self.x, self.y)
