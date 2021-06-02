# random rectangles
from random import choice, randint

WITH = 920
HEIGHT = 640
NO_RECT = 40
FPS = 60

# Farben
WHITE =  "#ffffff"
GREY =   "#444444"
ORANGE = "#ff9213"

colors = [WHITE, GREY, ORANGE]
rects = []
color_list = []

def setup():
    global counter, switch
    size(WITH, HEIGHT)
    this.surface.setTitle("Random Rectangles")
    background("#004477")
    for _ in range(NO_RECT):
        color_list.append(choice(colors))
        # Rechteckliste initialisieren
        rects.append([randint(10, width/2), randint(10, height/2),
                      randint(10, width - width/2 + 5), randint(10, height - height/2)])
        for i in range(len(rects)):
            for j in range(4):
                rect(rects[i][j])
    counter = 0
    switch = 10
    frameRate(FPS)
        
def draw():
    global counter, switch
    if counter >= switch:
        # Neues Farbe am Beginn der Liste einfügen
        color_list.insert(0, choice(colors))
        # Letztes Farbe am Ende der Liste löschen
        color_list.pop()
        # Neues Rechtekc am Beginn der Rechteckliste einfügen
        rects.insert(0, ((randint(10, width/2), randint(10, height/2),
                          randint(10, width - width/2 + 5), randint(10, height - height/2))))
        # Letztes Rechteck am Ende der Rechteckliste löschen
        rects.pop()
        # Rechtecke zeichnen
        for rectangle in rects:
            # fill(choice(color_list))
            rect(rectangle)
        
