from random import randint

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 15, 15

def setup():
    size(WIDTH, HEIGHT)
    this.windowTitle("Re-enactment Victor Vasarely")
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
            
            fill(randint(10, 180), randint(10, 180), randint(10, 180))
            rect(x, y, cellWidth, cellHeight)
            fill(randint(10, 230), randint(10, 230), randint(10, 230))
            dia = random(0.6, 0.9)
            # dia = 0.9
            ellipse(x, y, cellWidth*dia, cellHeight*dia)
    print("I did it, Babe!")
