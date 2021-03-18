# Processing(.py) Graphing Tool
# Inspired from »Visualizing Data« (Ben Fry) and
# »Math Adventures with Python« (Peter Farrell)

WIDTH = 720
HEIGHT = 450

def setup():
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Made a Graph")
    
    # Zeichenbereich
    plot_x1 = 50
    plot_x2 = width - plot_x1
    plot_y1 = 60
    plot_y2 = height - plot_y1

def draw():
    background(224)
    
    # Den Plot in einem weißen Kasten zeichnen
    fill(255)
    rectMode(CORNERS)
    noStroke()
    rect(plot_x1, plot_y1, plot_x2. plot_y2)
