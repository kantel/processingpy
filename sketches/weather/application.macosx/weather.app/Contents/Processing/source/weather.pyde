from getWeatherData import getWeatherData, getNow

def setup():
    size(600, 400)
    background(0)
    frame.setTitle (u"Jörgs Wetterstation")
    font = createFont("American Typewriter", 18)
    textFont(font)
    getWeatherData()
    getNow()
    frameRate(1)

def draw():
    if(second() == 0):
        background(0)
        getWeatherData()
        getNow()