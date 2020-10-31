class UnicornRainbow:
    
    def __init__(self):
        self.rainbow = []
        self.side = 6
        self.im = loadImage("unicorn.png")
        self.offset = 240
                                
    def add_rainbow_stripes(self):
        rectMode(CENTER)
        self.rainbow.append(([self.offset, mouseY + 48, self.side, self.side], color(240, 80, 37)))
        self.rainbow.append(([self.offset, mouseY + 54, self.side, self.side], color(248, 158, 80)))
        self.rainbow.append(([self.offset, mouseY + 60, self.side, self.side], color(248, 239, 34)))
        self.rainbow.append(([self.offset, mouseY + 66, self.side, self.side], color(49, 197, 244)))
        self.rainbow.append(([self.offset, mouseY + 72, self.side, self.side], color(240, 99, 164)))
        self.rainbow.append(([self.offset, mouseY + 78, self.side, self.side], color(129, 122, 198)))
    
    def delete_stripes(self):
        rainbow_copy = [stripe for stripe in self.rainbow if stripe[0][0] > 0]
        rainbow = rainbow_copy
        print(len(rainbow))
       
    def update(self):
        if self.rainbow:
            self.delete_stripes()
            for stripe in self.rainbow:
                stripe[0][0] -= 2
                
    def show(self):
        image(self.im, self.offset, mouseY)
        for stripe in self.rainbow:
            col = stripe[1]
            fill(col)
            noStroke()
            rect(stripe[0][0], stripe[0][1], stripe[0][2], stripe[0][3])
