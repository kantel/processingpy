# coding=utf-8
import json
import urllib2
import datetime

def getWeatherData():
    weatherUrl = "http://api.openweathermap.org/data/2.5/weather?q=Berlin%20Tempelhof,DE&units=metric&lang=de&APPID=5752bc935527151680eb4e04c03b8c8f"
    weatherData = json.load(urllib2.urlopen(weatherUrl))
    
    # Temperatur
    temp = weatherData["main"]["temp"]
    myTemperatur = u"Temperatur: " + str(temp) + u"°C."
    text(myTemperatur, 10, 20)
    
    # Wetter-Beschreibung
    wetter = weatherData["weather"][0]["description"]
    myWetter = u"Wetter: " + wetter + "."
    text(myWetter, 10, 40)
    
    # Sonnenauf- und -untergang
    sunrise = weatherData["sys"]["sunrise"]
    sunset = weatherData["sys"]["sunset"]
    mySunrise = "Sonnenaufgang: " + datetime.datetime.fromtimestamp(sunrise).ctime() + "."
    mySunset =  "Sonnenuntergang: " + datetime.datetime.fromtimestamp(sunset).ctime() + "."                             
    text(mySunrise, 10, 80)
    text(mySunset, 10, 100)
    
    # Luftdruck und -feuchtigkeit
    pressure = weatherData["main"]["pressure"]
    myPressure = "Luftdruck: " + str(pressure) + " hPa."
    text(myPressure, 10, 140)
    humidity = weatherData["main"]["humidity"]
    myHumidity = "Luftfeuchtigkeit: " + str(humidity) + " %."
    text(myHumidity, 10, 160)
    
    # Windgeschwindigkeit und Bewölkung
    wind = weatherData["wind"]["speed"]
    myWind = "Windgeschwindigkeit: " + str(wind) + " m/s."
    text(myWind, 10, 200)
    clouds = weatherData["clouds"]["all"]
    myClouds = u"Bewölkung: " + str(clouds) + " %."
    text(myClouds, 10, 220)
    
    # Wetter-Icon
    icon = weatherData["weather"][0]["icon"]
    weatherIcon = loadImage("http://openweathermap.org/img/w/" + icon + ".png")
    image(weatherIcon, 10, 260)
    
    # Abfragezeit und -ort
    dt = weatherData["dt"]
    station = weatherData["name"]
    myDt = "Stand : " + datetime.datetime.fromtimestamp(dt).ctime() + " aus " + station + "."
    text(myDt, 10, 360)