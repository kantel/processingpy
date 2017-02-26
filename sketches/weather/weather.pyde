from getWeatherData import getWeatherData
import datetime

def setup():
    size(600, 400)
    background(0)
    frame.setTitle (u"Jörgs Wetterstation")
    font = createFont("American Typewriter", 18)
    textFont(font)
    getWeatherData()
    frameRate(1)
    myNow = datetime.datetime.now()
    myHour = str(myNow.hour)
    myMinute = str(myNow.minute).rjust(2, "0")
    mySecond = str(myNow.second).rjust(2, "0")
    myTime = myHour + " : " + myMinute + " : " + mySecond              
    text(u"Start: " + myTime, 10, 380)

def draw():
    if(second() == 0):
        background(0)
        getWeatherData()
        myNow = datetime.datetime.now()
        myHour = str(myNow.hour)
        myMinute = str(myNow.minute).rjust(2, "0")
        mySecond = str(myNow.second).rjust(2, "0")
        myTime = myHour + " : " + myMinute + " : " + mySecond
        text(u"Update: " + myTime, 10, 380)