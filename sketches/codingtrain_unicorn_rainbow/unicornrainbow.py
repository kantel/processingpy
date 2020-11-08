class UnicornRainbow:
    
    def __init__(self):
        self.rainbow = []
        self.side = 6
        self.im = loadImage("unicorn.png")
        self.offset = 240
        self.offset_rainbow = self.offset + 30
                                
    def add_rainbow_stripes(self):
        rectMode(CENTER)
        self.rainbow.append(([self.offset_rainbow, mouseY + (self.side*7), self.side, self.side], color(240, 80, 37)))
        self.rainbow.append(([self.offset_rainbow, mouseY + (self.side*8), self.side, self.side], color(248, 158, 80)))
        self.rainbow.append(([self.offset_rainbow, mouseY + (self.side*9), self.side, self.side], color(248, 239, 34)))
        self.rainbow.append(([self.offset_rainbow, mouseY + (self.side*10), self.side, self.side], color(49, 197, 244)))
        self.rainbow.append(([self.offset_rainbow, mouseY + (self.side*11), self.side, self.side], color(240, 99, 164)))
        self.rainbow.append(([self.offset_rainbow, mouseY + (self.side*12), self.side, self.side], color(129, 122, 198)))
    
    def delete_stripes(self):
        rainbow_copy = [stripe for stripe in self.rainbow if stripe[0][0] >= 0]
        self.rainbow = rainbow_copy
        # print(len(self.rainbow))
       
    def update(self):
        if self.rainbow:
            self.delete_stripes()
            for stripe in self.rainbow:
                stripe[0][0] -= 2
                
    def show(self):    
        for stripe in self.rainbow:
            col = stripe[1]
            fill(col)
            noStroke()
            rect(stripe[0][0], stripe[0][1], stripe[0][2], stripe[0][3])
        image(self.im, self.offset, mouseY)
