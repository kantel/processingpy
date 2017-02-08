# Turmite

[![Turmite](images/turmite.jpg)](https://www.flickr.com/photos/schockwellenreiter/32407973340/)

## Quellcode

~~~python
south = 0
east  = 1
north = 2
west  = 3

on  = color(188, 0, 0)   # rot
off = color(0)           # schwarz

def setup():
    global x, y, dir
    size(600, 200)
    x = width/2
    y = height/2
    dir = north
    frame.setTitle("Turmite")
    background(0)
    frameRate(600)

def draw():
    global x, y, dir
    if (dir == south):
        y += 1
        if (y == height):
            y = 0
    elif (dir == east):
        x += 1
        if (x == width):
            x = 0
    elif (dir == north):
        if (y == 0):
            y = height - 1
        else:
            y -= 1
    elif (dir == west):
        if (x == 0):
            x = width - 1
        else:
            x -= 1
    
    if (get(x, y) == on):
        set(x, y, off)
        if (dir == south):
            dir = west
        else:
            dir -= 1
    else:
        set(x, y, on)
        if (dir == west):
            dir = south
        else:
            dir += 1
~~~

## Literatur

- A.K. Dewdney: *Turmiten*, in: Christoph Pöppe (Hg.): *Computer-Kurzweil IV, Spektrum der Wissenschaft Sonderheft 10*, 1990, Seiten 90-94