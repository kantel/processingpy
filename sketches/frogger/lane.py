from rectangle import Rectangle

class Lane(Rectangle):
    
    def __init__(self, index, c, t = SAFETY, n = 0, len = 0, spacing = 0, speed = 0, i = None)
    super(Rectangle, self).__init__(0, index*GRID, width, GRID)
    self.type = t
