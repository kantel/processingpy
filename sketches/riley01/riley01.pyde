from random import choice

riley_pal = [color(4, 21, 31),
             color(1, 155, 183), color(1, 155, 183),
             color(226, 107, 67), color(226, 107, 67),
             color(60, 76, 97), 
             color(144, 166, 215), color(144, 166, 215),
             color(240, 192, 68), color(240, 192, 68),
             color(240, 245, 248)]

def setup():
    size(480, 480)
    this.surface.setTitle("Hommage an Bridget Riley")
    noLoop()

def draw():
    for i in range(width/12):
        # stroke(0, 0, 0)
        noStroke()
        fill(choice(riley_pal))
        rect(i*width/40, 0, width/40, height)
        
    
