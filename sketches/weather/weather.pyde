from getWeatherData import getWeatherData

def setup():
    size(400, 200)
    background(0)
    frame.setTitle (u"Jörgs Wetterstation")
    font = createFont("American Typewriter", 18)
    textFont(font)
    getWeatherData()
    frameRate(1)
    text(u"Start …", 10, 180)

def draw():
    if(second() == 0):
        background(0)
        getWeatherData()
        text(u"Update …", 10, 180)