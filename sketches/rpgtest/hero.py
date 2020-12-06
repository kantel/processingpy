class Hero():
    
     
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.dir = None
        self.ts = 32        # Tilesize
        self.yoff = 80
        self.dir = "right"
        self.walking = False
        self.count = 0
        
        self.hero_images = [loadImage("knt1_bk1.gif"), loadImage("knt1_bk2.gif"),
                            loadImage("knt1_fr1.gif"), loadImage("knt1_fr2.gif"),
                            loadImage("knt1_lf1.gif"), loadImage("knt1_lf2.gif"),
                            loadImage("knt1_rt1.gif"), loadImage("knt1_rt2.gif")]
        self.hero_image = self.hero_images[6]
    
    def update(self):
        if self.dir == "right" and self.walking == True:
            if self.count == 0:
                self.hero_image = self.hero_images[6]
                self.pos.x += 0.25
            elif self.count == 5:
                self.hero_image = self.hero_images[7]
                self.pos.x += 0.25
            elif self.count == 10:
                self.hero_image = self.hero_images[6]
                self.pos.x += 0.25
            elif self.count == 15:
                self.hero_image = self.hero_images[7]
                self.pos.x += 0.25
            self.count += 1
            if self.count == 20:
                self.count = 0
                self.walking = False
                self.hero_image = self.hero_images[6]
        if self.dir == "left" and self.walking == True:
            if self.count == 0:
                self.hero_image = self.hero_images[4]
                self.pos.x -= 0.25
            elif self.count == 5:
                self.hero_image = self.hero_images[5]
                self.pos.x -= 0.25
            elif self.count == 10:
                self.hero_image = self.hero_images[4]
                self.pos.x -= 0.25
            elif self.count == 15:
                self.hero_image = self.hero_images[5]
                self.pos.x -= 0.25
            self.count += 1
            if self.count >= 20:
                self.count = 0
                self.walking = False
                self.hero_image = self.hero_images[4]
        if self.dir == "down" and self.walking == True:
            if self.count == 0:
                self.hero_image = self.hero_images[2]
                self.pos.y += 0.25
            elif self.count == 5:
                self.hero_image = self.hero_images[3]
                self.pos.y += 0.25
            elif self.count == 10:
                self.hero_image = self.hero_images[2]
                self.pos.y += 0.25
            elif self.count == 15:
                self.hero_image = self.hero_images[3]
                self.pos.y += 0.25
            self.count += 1
            if self.count == 20:
                self.count = 0
                self.walking = False
                self.hero_image = self.hero_images[2]
        if self.dir == "up" and self.walking == True:
            if self.count == 0:
                self.hero_image = self.hero_images[0]
                self.pos.y -= 0.25
            elif self.count == 5:
                self.hero_image = self.hero_images[1]
                self.pos.y -= 0.25
            elif self.count == 10:
                self.hero_image = self.hero_images[0]
                self.pos.y -= 0.25
            elif self.count == 15:
                self.hero_image = self.hero_images[1]
                self.pos.y -= 0.25
            self.count += 1
            if self.count >= 20:
                self.count = 0
                self.walking = False
                self.hero_image = self.hero_images[0]
   
    def show(self):
        image(self.hero_image, self.pos.x*self.ts, self.pos.y*self.ts + self.yoff)
