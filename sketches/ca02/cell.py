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
    
    def check_neighbors(self, clist):
        if self.state == 1: return(1)
        neighbs = 0
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            try:
                if clist[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if neighbs in [1, 4]:
            return(1)
        else:
            return(0)
            
    
