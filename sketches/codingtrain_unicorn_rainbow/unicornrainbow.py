class UnicornRainbow:
    
    def __init__(self):
        self.rainbow = []
        self.side = 12
        self.im = loadImage("unicorn.png")
                                
    def add_rainbow_stripes(self, offset, col):
        rectMode(CENTER)
        self.rainbow.append(([width - offset, mouseY, self.side, self.side], col))
    
    def delete_stripes(self):
        rainbow_copy = [stripe for stripe in self.rainbow if stripe[0][0] < 0]
        rainbow = rainbow_copy
       
    def update(self):
        if self.rainbow:
            self.delete_stripes()
            for stripe in self.rainbow:
                stripe[0][0] -= 2
                
    def show(self):
        image(self.im, width - 200, mouseY - 50)
        for stripe in self.rainbow:
            col = stripe[1]
            fill(col)
            noStroke()
            rect(stripe[0][0], stripe[0][1], stripe[0][2], stripe[0][3])
