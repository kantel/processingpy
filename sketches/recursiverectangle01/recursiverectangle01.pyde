def setup():
    size(500, 500)
    this.windowTitle("Quadrate rekursiv")
    background(235, 215, 182)  # Packpapier
    rectMode(CENTER)
    noFill()
    stroke(0)
    
    drawBox(width/2, height/2, width/2)
    
    print("I did it, Babe!")
    
def drawBox(cx, cy, d):
    strokeWeight(0.1*d)
    stroke(d)
    rect(cx, cy, d, d)
    
    if (d < 20): return
    
    drawBox(cx - d/2, cy - d/2, d/2)
    drawBox(cx + d/2, cy - d/2, d/2)
    drawBox(cx - d/2, cy + d/2, d/2)
    drawBox(cx + d/2, cy + d/2, d/2)
