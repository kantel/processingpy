from random import randint

WIDTH, HEIGHT = 600, 400
ROWS, COLS = 10, 15

codingtrain = ["#f05025", "#f89e50", "#f8ef22", "#31c5f4", "#f063a4",
               "#9252a1", "#817ac6", "#62c777"]

def setup():
    size(WIDTH, HEIGHT)
    this.windowTitle("Re-enactment Victor Vasarely (2)")
    # strokeWeight(2)
    noStroke()
    rectMode(CENTER)
    noLoop()
    
def draw():
    cellWidth = width/COLS
    cellHeight = height/ROWS
    
    for c in range(COLS):
        for r in range(ROWS):
            x = c*cellWidth + cellWidth/2
            y = r*cellHeight + cellHeight/2
            
            ci = randint(0, len(codingtrain) - 1)
            fill(codingtrain[ci])
            rect(x, y, cellWidth, cellHeight)
            fill(randint(20, 200))
            dia = random(0.6, 0.9)
            # dia = 0.9
            ellipse(x, y, cellWidth*dia, cellHeight*dia)
    print("I did it, Babe!")
