# hatter_pos (630, 65) (840, 300)
# march_hare_pos (380, 155) (540, 290)
# alice_pos (140, 190) (250, 340) 


def setup():
    global teaparty
    size(940, 530)
    this.surface.setTitle("Mad Hatters Tea Party")
    teaparty = loadImage("aliceteaparty.jpg")

def draw():
    image(teaparty, 0, 0, width, height)
    speech_bubble(675, 90, u"Macht Wunderland GROSS!")
    speech_bubble(230, 200, u"Kurios und kurioser …")

def speech_bubble(x, y, txt):
    # strokeWeight(1)
    noStroke()
    with pushMatrix():
        translate(x, y)
        # tail
        fill("#ffffff")
        with beginClosedShape():
            vertex(0, 0)  # tip
            vertex(15, -40)
            vertex(35, -40)
        # bubble
        textSize(15)
        by = -85
        bw = textWidth(txt)
        pad = 20
        rect(0, by, bw + pad*2, 45, 10)
        fill("#000000")
        textAlign(LEFT, CENTER)
        text(txt, pad, by + pad)
            
