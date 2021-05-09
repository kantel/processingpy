from random import randint, choice

riley_pal = [color(4, 21, 31), color(1, 155, 183), color(226, 107, 67),
             color(60, 76, 97), color(144, 166, 215), color(240, 192, 68),
             color(240, 245, 248)]
WIDTH = 640
HEIGHT = 480
FPS = 60
color_list = []

def setup():
    global counter, switch
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Hommage an Bridget Riley, animiert")
    # Initiale Farbliste erstellen
    for i in range(width/12):
        color_list.append(choice(riley_pal))
    switch = 10
    counter = 0
    frameRate(FPS)

def draw():
    global counter, switch
    noStroke()
    if counter >= switch:
        # Neue Farbe am Beginn der Liste einfügen
        color_list.insert(0, choice(riley_pal))
        # Letzte Farbe am Ende der Liste löschen
        color_list.pop()
        counter = 0
        switch = randint(10, 32)
        for i in range(width/12):
            fill(color_list[i])
            rect(i*width/40, 0, width/40, height)
    counter += 1
    # if frameCount <= 3600:
    #     saveFrame("pics/####.png")
    # else:
    #     print("I did it Babe")
    #     noLoop()
