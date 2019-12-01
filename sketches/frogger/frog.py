from rectangle import Rectangle

class Frog(Rectangle):
    
    def __init__(self, x, y, w):
        # super(Rectangle, self).__init__(x, y, w, w)
        self.x = x
        self.y = y
        self.w = w
        self.h = w
        self.img = loadImage("frog1.png")
        # self.attached = None
    
    def attach(self, log):
        self.attached = log
    
    def update(self):
        if self.attached:
            self.x += self.attached.speed
            self.x = constrain(self.x, 0, width-self.w)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x = constrain(self.x, 0, width-self.w)
        self.y = constrain(self.y, 0, height-self.h)
        self.attach(None)

    def show(self):
        image(self.img, self.x, self.y)
        
