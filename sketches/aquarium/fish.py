from random import randint

class Fish():
    
    def __init__(self, im):
        no = str(randint(1, 7))
        self.imr0 = loadImage(im + no + "_r0.png")
        self.iml0 = loadImage(im + no + "_l0.png")
        self.imr1 = loadImage(im + no + "_r1.png")
        self.iml1 = loadImage(im + no + "_l1.png")
        self.im = self.imr0
        self.speed = randint(-3, 3)
        if self.speed < 0:
            self.im = self.iml1
        elif self.speed == 0:
            self.speed = randint(1, 3)
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
        if self.pos.x >= width - self.w:
            self.speed = -randint(1, 3)
            self.im = self.iml0
        elif self.pos.x <= 0:
            self.speed = randint(1, 3)
            self.im = self.imr0
    
    def show(self):
        image(self.im, self.pos.x, self.pos.y)
