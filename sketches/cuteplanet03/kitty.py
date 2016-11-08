class Kitty(object):
    def __init__(self, temp_x, temp_y):
        self.x = temp_x
        self.y = temp_y
        self.radius_x = 50  # Bildbreite/2
        self.radius_y = 85  # Bildhoehe/2
        
    def loadPic(self):
        self.img = loadImage("horngirl.png")
    
    def move(self):
        self.x = mouseX - self.radius_x
        self.y = mouseY - self.radius_y
        
    def display(self):
        image(self.img, self.x, self.y)

