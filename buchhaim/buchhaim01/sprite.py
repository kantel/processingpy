tw = 16
th = 16
tileSize = 16

class Sprite(object):
    
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
    
class Hero(Sprite):
    