countries = [u"Afghanistan", u"Mali, Senegal", u"Kosovo",
             u"Türkei (Syrien, Irak)", u"Nordirak", u"Libanon",
             u"Lybische Küste", u"Dschibuti" u"Sudan, Südsudan"
             u"Somalia", u"Westsahara"]
numSoldiers = [971, 950, 532, 275, 147, 126, 104, 33, 23, 9, 4]
# Zahlen von hier: https://de.statista.com/infografik/8394/einsatzgebiete-bundeswehr/

def setup():
    global X1, Y1, X2, Y2
    size(640, 480)
    X1 = Y1 = 50
    X2 = width - 50
    Y2 = height - Y1

def draw():
    global X1, Y1, X2, Y2
    background(51)
    rectMode(CORNERS)
    fill(255)
    rect(X1, Y1, X2, Y2)
    