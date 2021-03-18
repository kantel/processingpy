# Farbpalette nach Bridget Riley (2)

riley2 = [color(230, 230, 230), color(235, 200, 55), color(115, 165, 215),
          color(155, 195, 80), color(230, 135, 170), color(230, 80, 70),  
          color(65, 80, 150)]

def setup():
    size(510, 400)
    this.surface.setTitle("Bridget Riley 2")
    noStroke()
    noLoop()

def draw():
    for i in range(17):
        fill(riley2[i%7])
        rect(i*width/17, 0, width/17, height)
        
