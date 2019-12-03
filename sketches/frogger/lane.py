from rectangle import Rectangle
from obstacle import Obstacle
from random import randint

SAFETY = 0
CAR = 1
FLOAT = 2
GRID = 40

obstacles = []

class Lane(Rectangle):
    
    def __init__(self, index, c, t = SAFETY, n = 0, l = 0, spacing = 0, speed = 0, i = ""):
        super(Rectangle, self).__init__(0, index*GRID, width, GRID)
        self.x = 0
        self.y = index*GRID
        self.w = width
        self.h = GRID
        self.type = t
        self.col = c
        self.n = n
        self.l = l
        self.speed = speed
        # print(i)
        if self.type != SAFETY:
            self.img = i
            self.spacing = spacing
            if self.speed > 0:
                self.spacing = -self.spacing
            for i in range(self.n):
                obstacles.append(Obstacle(randint(0, 360) + self.spacing*i, self.y, self.l*GRID, GRID, self.speed, self.img))
    
    def run(self):
        fill(self.col)
        noStroke()
        rect(self.x, self.y, self.w, self.h)
        for obstacle in obstacles:
            obstacle.show()
            obstacle.update()
        
