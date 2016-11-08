# coding=utf-8

class Kitty(object):
    def __init__(self, tempX, tempY):
        self.x = tempX
        self.y = tempY
        self.radiusX = 50  # Bildbreite/2
        self.radiusY = 85  # Bildhöhe/2
        
    def loadPic(self):
        self.img = loadImage("horngirl.png")
    
    def move(self):
        self.x = mouseX - self.radiusX
        self.y = mouseY - self.radiusY
        
    def display(self):
        image(self.img, self.x, self.y)

