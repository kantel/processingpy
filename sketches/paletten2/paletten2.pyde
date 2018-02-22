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

vaporwave    = ["#94d0ff", "#8795e8", "#966bff", "#ad8cff",
                "#c774e8", "#c774a9", "#ff6ad5", "#ff6a8b",
                "#ff8b8b", "#ffa58b", "#ffde8b", "#cdde8b",
                "#8bde8b", "#20de8b"]
cool         = ["#ff6ad5", "#c774e8", "#ad8cff", "#8795e8",
                "#94d0ff"]
crystalPepsi = ["#ffccff", "#f1daff", "#e3e8ff", "#ccffff"]
mallsoft     = ["#fbcff3", "#f7c0bb", "#acd0f4", "#8690ff",
                "#30bfdd", "#7fd4c1"]
jazzcup      = ["#392682", "#7a3a9a", "#3f86bc", "#28ada8",
                "#83dde0"]
sunset       = ["#661246", "#ae1357", "#f9247e", "#d7509f",
                "#f9897b"]
macplus      = ["#1b4247", "#09979b", "#75d8d5", "#ffc0cb",
                "#fe7f9d", "#65323e"]
seapunk      = ["#532e57", "#a997ab", "#7ec488", "#569874",
                "#296656"]

w = h = 64

def setup():
    size(480, 530)
    noLoop()
    
def draw():
    background("#2b3e50")
    j = 10
    for i in range(len(vaporwave)):
        fill(vaporwave[i])
        rect(i*w/2 + 8, j, w/2, h)
    j += h
    for i in range(len(cool)):
        fill(cool[i])
        rect(i*w + 8, j, w, h)
    j += h
    for i in range(len(crystalPepsi)):
        fill(crystalPepsi[i])
        rect(i*w + 8, j, w, h)
    j += h
    for i in range(len(mallsoft)):
        fill(mallsoft[i])
        rect(i*w + 8, j, w, h)
    j += h
    for i in range(len(jazzcup)):
        fill(jazzcup[i])
        rect(i*w + 8, j, w, h)
    j += h
    for i in range(len(sunset)):
        fill(sunset[i])
        rect(i*w + 8, j, w, h)
    j += h
    for i in range(len(macplus)):
        fill(macplus[i])
        rect(i*w + 8, j, w, h)
    j += h
    for i in range(len(seapunk)):
        fill(seapunk[i])
        rect(i*w + 8, j, w, h)
