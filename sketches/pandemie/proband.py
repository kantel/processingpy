# coding=utf-8

from random import randint

class Proband():
    
    def __init__(self, x, y, zustand):
        self.x = x
        self.y = y
        self.sz = 5
        self.move = 10
        self.zustand = zustand
    
    def update(self):
        if self.zustand > 1:
            self.zustand -= 1
        if self.zustand == 1:
            self.zustand = -1
        self.x += randint(-self.move, self.move)
        self.y += randint(-self.move, self.move)
        if self.x >= width - 2*self.sz:
            self.x = width - 2*self.sz
        if self.y >= height - 2*self.sz:
            self.y = height - 2*self.sz
        if self.x <= self.sz:
            self.x = self.sz
        if self.y <= self.sz:
            self.y = self.sz
        if self.zustand > 10:     # Krank
            fill(200, 0, 0, 100)
        if self.zustand == 0:    # Gesund
            fill(0, 100, 0, 100)
        if self.zustand == -1:
            fill(200, 200, 0, 100) # Immun
        circle(self.x, self.y, 2*self.sz)
        
    def collision(self, other):
        if self != other:
            distance = dist(self.x, self.y, other.x, other.y)
            if distance <= self.sz + other.sz:
                # return True
                if other.zustand > 1 and self.zustand == 0:
                    self.zustand = 30
            
