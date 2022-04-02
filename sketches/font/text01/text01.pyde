margin = 10

def setup():
    size(500, 500)
    this.windowTitle(u"Seltsame Zeichen 🤡")
    this.windowMove(1400, 30)
    noLoop()

def draw():
    background(255)
    fill(30)
    noStroke()
    rect(margin, margin, width - 2*margin, height - 2*margin)
    font = createFont("ComicHelvetic-Heavy", 58)
    textFont(font)
    textSize(52)
    fill(127, 199, 175)
    u = 70
    text("Seltsame Zeichen", 20, u)
    u = 110
    font = createFont("Comic Helvetic", 24)
    textFont(font)
    textSize(24)
    fill(237, 118, 112)
    lines = loadStrings("boxer.txt")
    for line in lines:
        print(line)
        text(line, 20, u, 460, 500)
        u += 80
    
