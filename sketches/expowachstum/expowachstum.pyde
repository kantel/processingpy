# Exponentielles Wachstum

import math

WIDTH = 720
HEIGHT = 450

dt = 0.05

# Zeichenbereich
plot_x1 = 120
plot_x2 = WIDTH - 80 # WIDTH - plot_x1
label_x = 50
plot_y1 = 60
plot_y2 = HEIGHT - plot_y1
label_y = HEIGHT - 25

# Titel
plot_title = u"Exponentielles Wachstum"

# Funktionsabhängige Konstanten
x_min = 0
x_max = 25
y_min = 0
y_max = 260000
stepsize_x = 5   # Ticks auf der x-Achse
stepsize_y = -20000  # Ticks auf der y-Achse
r = 0.5 # Wachstumsrate

def setup():
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Exponentielles Wachstum")
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
    draw_axis_labels()
    draw_function()
    print("I did it, Babe!")
    
def f(t):
    return(math.exp(r*t))

def draw_function():
    stroke(255, 0, 0)
    t = x_min
    while t <= x_max - dt:
        x_0 = map(t, x_min, x_max, plot_x1, plot_x2)
        x_1 = map(t + dt, x_min, x_max, plot_x1, plot_x2)
        y_0 = map(f(t), y_min, y_max, plot_y2, plot_y1)
        y_1 = map(f(t + dt), y_min, y_max, plot_y2, plot_y1)
        line(x_0, y_0, x_1, y_1)
        t += dt
    
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

def draw_axis_labels():
    fill(0, 150, 0)
    textSize(13)
    textLeading(15)
    textAlign(CENTER, CENTER)
    text("Anzahl", label_x, (plot_y1 + plot_y2)/2)
    textAlign(CENTER)
    text(u"Zeit", (plot_x1 + plot_x2)/2, label_y)
    
