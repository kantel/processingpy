# coding=utf-8
from config import Settings

s = Settings()

class Grass():
    
    def __init__(self, x, y, sz):
        self.x = x
        self.y = y
        self.energy = 5
        self.eaten = False
        self.sz = sz
    
    def update(self):
        noStroke()
        if self.eaten:
            if random(1000) < 5:
                self.eaten = False
            else:
                fill(s.BROWN)
        else:
            fill(s.GREEN)
        rect(self.x, self.y, self.sz, self.sz)
