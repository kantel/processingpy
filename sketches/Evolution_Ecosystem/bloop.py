from dna import DNA

class Bloop(object):

    def __init__(self, dna, loc):
        self.location = loc
        self.dna = dna
        self.lifespan = 255
        self.maxspeed = map(self.dna.genes[0], 0.0, 1.0, 15, 0)
        self.r = map(self.dna.genes[0], 0.0, 1.0, 0, 50)
        self.xoff = random(1000)
        self.yoff = random(1000)

    def update(self):
        vx = map(noise(self.xoff), 0, 1, -self.maxspeed, self.maxspeed)
        vy = map(noise(self.yoff), 0, 1, -self.maxspeed, self.maxspeed)
        self.velocity = PVector(vx, vy)
        self.xoff += 0.01
        self.yoff += 0.01
        self.location.add(self.velocity)
        if self.location.x > width + self.r:
            self.location.x = -self.r
        elif self.location.x < - self.r*2:
            self.location.x = width + self.r
        if self.location.y > height + self.r:
            self.location.y =  -self.r
        elif self.location.y < -self.r:
            self.location.y = height + self.r
        

        self.lifespan -= 0.2

    def display(self):
        ellipseMode(CENTER)
        stroke(0)
        fill(0, self.lifespan)
        ellipse(self.location.x, self.location.y, self.r, self.r)
    
    def run(self):
        self.update()
        self.display()

    def eat(self, food):
        for i in range(len(food) - 1, -1, -1):
            # foodloc = PVector(food[i].x, food[i].y)
            d = PVector.dist(self.location, food[i])
            if d < self.r / 2:
                self.lifespan += 100
                if self.lifespan >= 255:
                    self.lifespan = 255
                food.pop(i)

    def reproduce(self):
        self.childDNA = DNA()
        self.childDNA = self.dna.copy(self.dna.genes[:])
        # childDNA.mutate(0.01)
        return Bloop(self.childDNA, self.location)

    def isDead(self):
        if self.lifespan <= 0:
            return True
        else:
            return False
