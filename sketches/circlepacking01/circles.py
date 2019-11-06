class Circle(object):
    
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        self.r = 1
        self.growing = True
        
    def grow(self):
        if self.growing:
            self.r += 0.5
    
    def edges(self):
        return(self.x + self.r > width or self.x - self.r < 0 or
               self.y + self.r > height or self.y - self.r < 0)
   
    def show(self):
        fill(self.c)
        noStroke()
        # strokeWeight(1)
        ellipse(self.x, self.y, self.r*2, self.r*2) 
