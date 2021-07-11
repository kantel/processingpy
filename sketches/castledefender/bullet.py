import math

class Bullet():
    
    def __init__(self, x, y, angle):
        self.img = loadImage("bullet.png")
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10
        self.delete = False
        self.b_w = 12  # Bullet width
        self.b_h = 11  # Bullet height
        self.dx = math.sin(self.angle) * self.speed
        self.dy = -(math.cos(self.angle) * self.speed)
    
    def update(self):
        if self.x + self.b_w < 0 or self.x > width or self.y + self.b_h < 0 or self.y > height:
            # print("Delete Bullet")
            self.delete = True
        self.x += self.dx
        self.y += self.dy
    
    def show(self):
        image(self.img, self.x, self.y)
