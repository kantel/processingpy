from random import randint

class Fish():
    
    def __init__(self):
        no = str(randint(1, 7))
        self.imr0 = loadImage("fish" + no + "_r0.png")
        self.iml0 = loadImage("fish" + no + "_l0.png")
        self.imr1 = loadImage("fish" + no + "_r1.png")
        self.iml1 = loadImage("fish" + no + "_l1.png")
        self.reset()
        self.w = self.h = 32
        self.pos = PVector(randint(30, width - 30), randint(10, height - 120))
        self.count = 0
        self.switch = 5
    
    def update(self):
        self.pos.x += self.speed
        self.count -= 1
        if self.count <= 0:
            self.count = self.switch
            if self.im == self.imr0:
                self.im = self.imr1
            elif self.im == self.imr1:
                self.im = self.imr0
            elif self.im == self.iml0:               
                self.im = self.iml1
            elif self.im == self.iml1:
                self.im = self.iml0
        if self.pos.x > width + 2*self.w:
            self.pos.x = randint(width + self.w, width + 2*self.w)
            self.pos.y = randint(10, height - 120)
            self.speed = -randint(1, 3)
            self.im = self.iml0
        elif self.pos.x < -2*self.w:
            self.pos.x = randint(-2*self.w, -self.w)
            self.pos.y = randint(10, height - 120)
            self.speed = randint(1, 3)
            self.im = self.imr0
    
    def show(self):
        image(self.im, self.pos.x, self.pos.y)
    
    def reset(self):
        self.im = self.imr0
        self.speed = randint(-3, 3)
        if self.speed < 0:
            self.im = self.iml1
        elif self.speed == 0:
            self.speed = randint(1, 3)
