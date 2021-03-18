# Processing(.py) Graphing Tool
# Inspired from »Visualizing Data« (Ben Fry) and
# »Math Adventures with Python« (Peter Farrell)

import math

WIDTH = 720
HEIGHT = 450

dt = 0.05

# Zeichenbereich
plot_x1 = 50
plot_x2 = WIDTH - plot_x1
plot_y1 = 60
plot_y2 = HEIGHT - plot_y1

# Titel
plot_title = u"Sinuskurve"

# Funktionsabhängige Konstanten
x_min = -10
x_max = 10
y_min = -2
y_max = 2
stepsize_x = 2   # Ticks auf der x-Achse
stepsize_y = -1  # Ticks auf der y_Achse

def setup():
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Funktionsplotter")
    plot_font = createFont("American Typewriter", 20)
    textFont(plot_font)
    noLoop()
    
def draw():
    background(234, 218, 184)
    # Den Plot in einem weißen Kasten zeichnen
    fill(255)
    rectMode(CORNERS)
    noStroke()
    rect(plot_x1, plot_y1, plot_x2, plot_y2)
    # Title des Plots
    fill(0, 150, 0)
    textSize(20)
    textAlign(LEFT)
    text(plot_title, plot_x1, plot_y1 - 10)
    draw_grid()
    draw_function()
    print("I did it, Babe!")
    
def f(x):
    return(math.sin(x))

def draw_function():
    stroke(255, 0, 0)
    x = x_min
    while x <= x_max - dt:
        # print(f(col))
        x_0 = map(x, x_min, x_max, plot_x1, plot_x2)
        x_1 = map(x + dt, x_min, x_max, plot_x1, plot_x2)
        y_0 = map(f(x), y_min, y_max, plot_y2, plot_y1)
        y_1 = map(f(x + dt), y_min, y_max, plot_y2, plot_y1)
        line(x_0, y_0, x_1, y_1)
        x += dt
    
def draw_grid():
    # Zeichnet Gitter und Label
    textSize(10)
    textAlign(CENTER, TOP)
    # x-Achse
    for i in range(x_min, x_max + 1, stepsize_x):
        x = map(i, x_min, x_max, plot_x1, plot_x2)
        fill(0, 150, 0)
        text(str(i), x, plot_y2 + 10)
        strokeWeight(1)
        stroke(0, 255, 255)
        line(x, plot_y1, x, plot_y2)
    # y-Achse
    for j in range (y_max, y_min - 1, stepsize_y):
        y = map(j, y_max, y_min, plot_y1, plot_y2)
        if j == y_min:
            textAlign(RIGHT, BOTTOM)  # Unten
        elif j == y_max:
            textAlign(RIGHT, TOP)     # Oben
        else:
            textAlign(RIGHT, CENTER)  # Vertikal zentrieren
        fill(0, 150, 0)
        text(str(j), plot_x1 - 10, y)
        strokeWeight(1)
        stroke(0, 255, 255)
        line(plot_x1, y, plot_x2, y)
    
