class Viehicle():
    
    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, 0)
        self.location = PVector(x, y)
        self.r = 8.0
        self.maxspeed = 5
        self.maxforce = 0.1
        self.d = 25
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
    
    def applyForce(self, force):
        self.acceleration.add(force)
        
    def seek(self, target):
        desired = PVector.sub(target, self.location)
        # Check Boundaries
        if self.location.x < self.d:
            desired = PVector(self.maxspeed, self.velocity.y)
        elif self.location.x > width - self.d:
            desired = PVector(-self.maxspeed, self.velocity.y)
        if self.location.y < self.d:
            desired = PVector(self.velocity.x, self.maxspeed)
        elif self.location.y > height - self.d:
            desired = PVector(self.velocity.x, -self.maxspeed)
        desired.normalize()
        desired.mult(self.maxspeed)
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)
        self.applyForce(steer)
   
    def display(self):
        theta = self.velocity.heading() + PI/2
        fill(color(98, 199, 119))
        stroke(1)
        strokeWeight(1)
        with pushMatrix():
            translate(self.location.x, self.location.y)
            rotate(theta)
            with beginShape():
                vertex(0, -self.r*2)
                vertex(-self.r, self.r*2)
                vertex(self.r, self.r*2)
        
