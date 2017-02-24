# coding=utf-8
import json
import urllib2

def getWeatherData():
    weatherUrl = "http://api.openweathermap.org/data/2.5/weather?q=Berlin%20Tempelhof,DE&units=metric&lang=de&APPID=5752bc935527151680eb4e04c03b8c8f"
    weatherData = json.load(urllib2.urlopen(weatherUrl))
    temp = weatherData["main"]["temp"]
    myTemperatur = u"Temperatur: " + str(temp) + u"°C."
    text(myTemperatur, 10, 20)
    wetter = weatherData["weather"][0]["description"]
    myWetter = u"Wetter: " + wetter + "."
    text(myWetter, 10, 40)
