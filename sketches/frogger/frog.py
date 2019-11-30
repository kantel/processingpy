from rectangle import Rectangle

class Frog(Rectangle):
    
    def __init__(self, x, y, w):
        # super(Rectangle, self).__init__(x, y, 40, 40)
        self.x = x
        self.y = y
        self.w = w
        self.h = w
        self.img = loadImage("frog1.png")

    def show(self):
        image(self.img, self.x, self.y)
        
