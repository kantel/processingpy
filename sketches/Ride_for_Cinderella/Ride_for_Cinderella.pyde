add_library('video')

def setup():
    global movie
    size(640, 480)
    movie = Movie(this, "RideforC1937.mp4")
    movie.loop()

def movieEvent(movie):
    movie.read()

def draw():
    image(movie, 0, 0)
