from random import randint

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10

def setup():
    size(WIDTH, HEIGHT)
    this.windowTitle("Random Flowers in a Grid")
    strokeWeight(2)
    noLoop()

def draw():
    background(235, 215, 182)  # Packpapier
    cellWidth = width/COLS
    cellHeight = height/ROWS
    
    for c in range(COLS):
        for r in range(ROWS):
            x = c*cellWidth + cellWidth/2
            y = r*cellHeight + cellHeight/2
            
            drawFlower(x, y, min(cellWidth, cellHeight))
    
    print("I did it, Babe!")
            
def drawFlower(x, y, s):
    flowerSize = random(s*0.5, s*0.95)
    petalSize = flowerSize/2
    spacing = petalSize*0.45
    
    fill(randint(10, 200), randint(10, 200), randint(10, 200))
    circle(x - spacing, y - spacing, petalSize)
    circle(x + spacing, y - spacing, petalSize)
    circle(x - spacing, y + spacing, petalSize)
    circle(x + spacing, y + spacing, petalSize)
    
    fill(randint(10, 200), randint(10, 200), randint(10, 200))
    circle(x, y, petalSize)
