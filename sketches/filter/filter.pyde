palette = ["#B83D4E", "#B56A8C", "#4688B5", "#A53643",
           "#5869A0", "#487A9C", "#95577E", "#302D32"] 
           # #0C0000 #020100 #070707

def setup():
    global jojo
    size(640, 320)
    jojo = loadImage("jojo.jpg")
    jojo.filter(THRESHOLD, 0.55)

def draw():
    global jojo
    background(51)
    for i in range(len(palette)):
        if (i < 4):
            row = 0
            j = i
        else:
            row = 160
            j = i - 4
        image(jojo, j*160, row)