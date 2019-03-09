add_library('box2d_processing')
# add_library('jbox2d')

class Box():
    
    def __init__(self, box2d, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
        
        bd = BodyDef()
        bd.type = BodyType.DYNAMIC
        bd.position.set(box2d.coordPixelsToWorld(self.x, self.y))
        self.body = box2d.createBody(bd)
        
        sd = box2d.PolygonShape()
        box2dW = box2d.scalarPixelsToWorld(self.w/2)
        box2dH = box2d.scalarPixelsToWorld(self.h/2)
        sd.setAsBox(box2dW, box2dH)
        
        fd = FixtureDef()
        fd.shape = sd
        fd.density = 1
        fd.friction = 0.3
        fd.restitution = 0.5
        
        self.body.createFixture(fd)
        
    def display(self):
        pos = box2d.getBodyPixelCoord(self.body)
        a = self.body.getAngle()
        
        with pushMatrix():
            translate(pos.x, pos.y)
            rotate(-a)
            fill(175)
            stroke(0)
            rectMode(CENTER)
            rect(0, 0, self.w, self.h)
