from viehicle import Viehicle

d = 25

def setup():
    global v, debug
    size(940, 295)
    this.surface.setTitle("Viehicle Part 2")
    v = Viehicle(width/2, height/2)
    debug = False
    
def draw():
    global v, debug
    background(color(146, 82, 161))
    
    if debug:
        stroke(175)
        noFill()
        rectMode(CENTER)
        rect(width/2, height/2, width - d*2, height - d*2)
        
    target = PVector(mouseX, mouseY)
    
    fill(color(248, 239, 34))
    stroke(1)
    strokeWeight(2)
    circle(target.x, target.y, 30)
    
    v.arrive(target)
    v.update()
    v.display()

def mousePressed():
    global debug
    debug = not debug
    
