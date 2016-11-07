# Hallo Kitty
font = None
greetings = u'Hallo Hörnchen!'

def setup():
    # Uncomment the following two lines to see the available fonts
    # fontList = PFont.list()
    # print(fontList)
    global img
    size(640, 480)
    img = loadImage("horngirl.png")
    font = createFont("Verdana-Bold", 64)
    # font = createFont("OpenSans-Semibold-webfont.ttf", 64)
    textFont(font)

def draw():
    background(0, 80, 125)
    image(img, 275, 100)
    text(greetings, 25, 350)