add_library('box2d_processing')
# add_library('jbox2d')

from box import Box

boxes = []

def setup():
    global box2d
    size(400, 300)
    box2d = Box2DProcessing(this)
    box2d.createWorld()

def draw():
    background(255)
    box2d.step()
    
    if mousePressed:
        box = Box(box2d, mouseX, mouseY)
        boxes.append(b)
