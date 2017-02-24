from getWeatherData import getWeatherData

def setup():
    size(400, 200)
    background(0)
    frame.setTitle (u"Jörgs Wetterstation")
    font = createFont("American Typewriter", 18)
    textFont(font)
    getWeatherData()
    frameRate(1)

def draw():
    
    if((minute() % 15 == 0) and (second() == 1)):
        background(0)
        getWeatherData()
