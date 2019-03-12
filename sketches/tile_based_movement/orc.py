# coding=utf-8
import time

TILESIZE = 32

class Orc():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.from_x = 0
        self.from_y = 0
        self.offset_x = 0
        self.offset_y = 0
        self.dir = "right"
        self.frame = 0
        self.sz = TILESIZE
        self.images = {}

    def loadPics(self):
        self.orcrt1 = loadImage("orcrt1.gif")
        self.orcrt2 = loadImage("orcrt2.gif")
        self.orcfr1 = loadImage("orcfr1.gif")
        self.orcfr2 = loadImage("orcfr2.gif")
        self.orclf1 = loadImage("orclf1.gif")
        self.orclf2 = loadImage("orclf2.gif")
        self.orcbk1 = loadImage("orcbk1.gif")
        self.orcbk2 = loadImage("orcbk2.gif")
        self.images = {
            "left": [self.orclf2, self.orclf1, self.orclf2,
                     self.orclf1, self.orclf2],
            "right": [self.orcrt2, self.orcrt1, self.orcrt2,
                      self.orcrt1, self.orcrt2],
            "up": [self.orcbk2, self.orcbk1, self.orcbk2,
                   self.orcbk1, self.orcbk2],
            "down": [self.orcfr2, self.orcfr1, self.orcfr2,
                     self.orcfr1, self.orcfr2]
        }

    def move(self):
        self.old_x = self.x
        self.old_y = self.y
        if self.frame > 0:
            self.frame += 1
            time.sleep(0.1)
            if self.frame == 5:
                self.frame = 0
                self.offset_x = 0
                self.offset_y = 0

        if self.dir == "right" and self.frame > 0:
            self.offset_x = -1 + (0.25 * self.frame)
        if self.dir == "left" and self.frame > 0:
            self.offset_x = 1 - (0.25 * self.frame)
        if self.dir == "up" and self.frame > 0:
            self.offset_y = 1 - (0.25 * self.frame)
        if self.dir == "down" and self.frame > 0:
            self.offset_y = -1 + (0.25 * self.frame)
            
    def display(self):
        image(self.images[self.dir][self.frame], self.x * self.sz + self.offset_x * self.sz,
              self.y * self.sz + self.offset_y * self.sz)
