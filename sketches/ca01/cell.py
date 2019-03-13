# coding=utf-8

class Cell():
    
    def __init__(self, c, r, sz, state = 0):
        self.c = c
        self.r = r
        self.sz = sz
        self.state = state
    
    def display(self):
        if self.state == 1:
            fill(0)   # schwarz
        else:
            fill(255)   # weiß
        rect(self.sz*self.r, self.sz*self.c, self.sz, self.sz)
    
