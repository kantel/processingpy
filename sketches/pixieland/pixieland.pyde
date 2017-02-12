font = None
headline = "OVER IN THE PIXIELAND"
para = "the quick brown fox jumps over the lazy dog"

def setup():
    global h1, pl
    size(600, 400)
    frame.setTitle("Pixieland")
    h1 = createFont("pixie-fat.otf", 32)
    # pu = createFont("pixie-semibold.otf", 16)
    pl = createFont("pixie-serif.otf", 32)
    background(80)
    noLoop()
    
def draw():
    global h1, pl
    textFont(h1)
    text(headline, 10, 100)
    textFont(pl)
    # fill(0)
    stroke(0)
    strokeWeight(1)
    text(para, 10, 200)