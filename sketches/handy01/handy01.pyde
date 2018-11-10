add_library('handy')

def setup():
    global h
    size(300, 200)
    h = HandyRenderer(this)

def draw():
    background(235, 215, 182)
    h.rect(75, 50, 150, 100)
