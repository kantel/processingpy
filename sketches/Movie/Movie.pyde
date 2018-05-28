add_library('video')

def setup():
    global movie
    size(560, 315)
    movie = Movie(this, "confettisystem.mp4")
    movie.loop()

def movieEvent(movie):
    movie.read()

def draw():
    global movie
    image(movie, 0, 0)
