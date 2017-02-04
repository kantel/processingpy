# with-Statement

def setup():
    size(400, 400)
    background(255)
    

def draw():
    fill(color(255,  153,  0))
    ellipse(100, 100, 50, 50)
    
    with pushStyle():
        fill(color(255,  51,  51))
        strokeWeight(5)
        ellipse(200, 200, 50, 50)
        
    ellipse(300, 300, 50, 50)
