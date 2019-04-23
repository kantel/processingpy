add_library('peasycam')

def setup():
    size(600, 600, OPENGL)
    cam = PeasyCam(this, 1000)

def draw():
    background(235)
    stroke(0)
    noFill()
    box(600)
