add_library('opencv_processing')

faces = []

def setup():
    global opencv, faces
    size(640, 480)
    opencv = OpenCV(this, "puppen.jpg")
    
    opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE)
    faces = opencv.detect()
    # print(len(faces))
    
def draw():
    global opencv, faces
    image(opencv.getInput(), 0, 0)
    noFill()
    stroke(0, 255, 0)
    strokeWeight(2)
    for i in range(len(faces)):
        rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height)
    
