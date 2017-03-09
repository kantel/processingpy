countries = [u"Afghan", u"Mali", u"Kosovo",
             u"Türkei", u"Irak", u"Liban",
             u"Lybien", u"Dschib", u"Sudan",
             u"Somal", u"Sahara"]
numSoldiers = [971, 950, 532, 275, 147, 126, 104, 33, 23, 9, 4]
# Zahlen von hier: https://de.statista.com/infografik/8394/einsatzgebiete-bundeswehr/
palette = [color(0, 100, 0), color(189, 183, 107), color(85, 107, 47),
           color(107, 142, 35), color(139, 69, 0), color(255, 140, 0),
           color(139, 71, 38), color(139, 0, 0), color(178, 34, 34),
           color(139, 26, 26), color(205, 0, 0)]
title = u"Anzahl deutscher Soldaten im Ausland nach Ländern und Einsatzgebieten"

def setup():
    size(640, 480)

def draw():
    x = width*0.1
    y = height*0.88
    delta = width*0.8/len(numSoldiers)
    w = delta*0.8
    background(255)
    fill(51)
    text(title, 120, 20)
    for i in range(len(numSoldiers)):
        # Zuerst die Höhe der Säulen berechnen
        h = map(numSoldiers[i], 0, 1200, 0, height)
        fill(palette[i])
        rect(x, y-h, w, h)
        text(countries[i], x, height-35)
        text(str(numSoldiers[i]), x, height-20)
        x += delta
    