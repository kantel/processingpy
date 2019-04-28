# coding=utf-8

class Alien(object):
    
    def __init__(self, x, y, im):
        self.x = x
        self.y = y
        self.im = im
        
    def update(self):
        pass
    
    def show(self):
        image(self.im, self.x, self.y)
