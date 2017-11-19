"""
tempsColor ist eine Palette zur Visualisierung von
Temperaturen (kalt bis heiß)
precsColor ist eine Palette zur Visualisierung von
Niederschlagsmengen (trocken bis naß) und
superColors sind einfach Farben aus Thomas Parks
Superhero-Theme für Bootstrap.
Quelle: Duncan M. Mc Greggor: Mastering matplotlib,
Birmingham (Packt Publishing) 2015
"""

tempsColors = ["#fcf8d4", "#faeab9", "#fad873",
               "#ffa500", "#ff8c00", "#b22222"]
precsColors = ["#f2d98f", "#f8ed39", "#a7cf38", "#7fc242",
               "#4680c2", "#3a53a3", "#6e4a98"]
superColors = ["#df691b", "#5cb85c", "#5bc0de",
               "#f0ad4e", "#d9534f", "#4e5d6c"]
w = h = 64

def setup():
    size(480, 210)
    noLoop()
    
def draw():
    background("#2b3e50")
    j = 10
    for i in range(len(tempsColors)):
        fill(tempsColors[i])
        rect(i*w + 8, j, w, h)
    j += h
    for i in range(len(precsColors)):
        fill(precsColors[i])
        rect(i*w + 8, j, w, h)
    j += h
    for i in range(len(superColors)):
        fill(superColors[i])
        rect(i*w + 8, j, w, h)
        