from bullet import Bullet

class Castle():
    
    def __init__(self, img):
        self.health = 1000
        self.max_health = self.health
        self.fired = False
        self.img = loadImage(img)
        self.x = width - 230
        self.y = height - 320
        self.mid_y = self.y + 120
            
    def show(self):
        image(self.img, self.x, self.y)
