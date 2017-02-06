font = None
tt = u"Zwölf Boxkämpfer jagen Eva quer über den großen Sylter Deich."

def setup():
    # frame.setTitle("Hallo UTF-8")
    size(800, 100)
    font = createFont("American Typewriter", 20)
    textFont(font)

def draw():
    background(255)
    fill(0)
    text(tt, 25, 50)