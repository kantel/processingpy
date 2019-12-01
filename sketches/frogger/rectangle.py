class Rectangle(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x = constrain(self.x, 0, width-self.w)
        self.y = constrain(self.y, 0, height-self.h)
    
    def intersects(self, other):
        distanceX = (self.x + self.w/2) - (other.x + other.w/2)
        distanceY = (self.y + self.h/2) - (other.y + other.h/2)
        halfW = self.w/2 + other.w/2
        halfH = self.h/2 + other.h/2
        if (abs(distanceX) < halfW):
            if (abs(distanceY) < halfH):
                return True
        return False
