add_library('opencv_processing')

contours = []

def setup():
    global jojosrc, jojodst, contours
    size(840, 420)
    jojosrc = loadImage("jojo2.jpg")
    opencv = OpenCV(this, jojosrc)
    
    opencv.gray()
    opencv.threshold(120)
    jojodst = opencv.getOutput()
    
    contours = opencv.findContours()
    print(contours.size())

def draw():
    global jojosrc, jojodst, contours
    image(jojosrc, 0, 0)
    image(jojodst, jojosrc.width, 0)
    
    noFill()
    strokeWeight(1)
    
    for contour in contours:
        stroke(0, 255, 0)
        contour.draw()
    
        stroke(255, 0, 0)
        point = PVector()
        beginShape()
        for point in contour.getPolygonApproximation().getPoints():
            vertex(point.x, point.y)
        endShape()

    
