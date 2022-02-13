from random import randint

WIDTH, HEIGHT = 640, 360
COLS, ROWS = 16, 9

vinik24 = ["#000000", "#6f6776", "#9a9a97", "#c5ccb8", "#8b5580",
           "#c38890", "#a593a5", "#666092", "#9a4f50", "#c28d75",
           "#7ca1c0", "#416aa3", "#8d6268", "#be955c", "#68aca9",
           "#387080", "#6e6962", "#93a167", "#6eaa78", "#557064",
           "#9d9f7f", "#7e9e99", "#5d6872", "#433455"]
def setup():
    size(WIDTH, HEIGHT)
    this.windowTitle("Re-enactment Victor Vasarely (3)")
    noStroke()
    rectMode(CENTER)
    frameRate(1)
    
def draw():
    cellWidth = width/COLS
    cellHeight = height/ROWS
    
    for c in range(COLS):
        for r in range(ROWS):
            x = c*cellWidth + cellWidth/2
            y = r*cellHeight + cellHeight/2
            
            ci = randint(0, len(vinik24) - 1)
            fill(vinik24[ci])
            rect(x, y, cellWidth, cellHeight)
            fill(randint(10, 230), randint(10, 230), randint(10, 230))
            dia = random(0.6, 0.9)
            ellipse(x, y, cellWidth*dia, cellHeight*dia)
    if frameCount <= 72:
        saveFrame("pics/####.png")
    else:
        print("I did it Babe")
        noLoop()
