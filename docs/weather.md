# Einen eigenen Wetterbericht mit OpenWeatherMap

![OpenWeatherMap Logo](images/OpenWeatherMapLogo.png)

## OpenWeatherMap

[OpenWeatherMap](http://openweathermap.org/) bietet aktuelle und freie ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)) Wetterdaten von mehr als 200.000 Stationen weltweit (sagt die [Wikipedia](https://de.wikipedia.org/wiki/OpenWeatherMap)), die über eine frei nutzbare [JSON-API](http://openweathermap.org/api) abgefragt werden können -- allerdings wird eine Registrierung und ein API-Key benötigt und um einen Rücklink auf OpenWeastherMap gebeten. Mit dem freien API-Key darf man 60 Anfragen in der Minute stellen und es stehen einem die

- Current Weather API, die
- 5 day/3 hour forecast API und die
- Weather maps API

zur Verfügung. Benötigt man mehr, muß man eine der kommerziellen Lizenzen nutzen. Man kann die APIs nach Städtenamen, Geo-Koordinaten oder Städte-IDs abfragen. Ich habe für mich mal ein paar relevante Orte herausgesucht:

- Berlin Tempelhof,DE -- Geo-Koordinaten [52.4769, 13.4103] (das ist die nächste Station an meinem Wohnort)
- Berlin Steglitz Zehlendorf,DE -- Geo-Koordinaten [52.4348, 13.2418]
- Schmargendorf,DE -- Geo-Koordinaten [52.4752, 13.2907] (ich weiß nicht, welche von den beiden näher an meiner Arbeitsstelle stationiert sind, Schmargendorf steht übrigens für Berlin Dahlem)
- Berlin Koepenick,DE -- Geo-Koordinaten [52.4425, 13.5823] (da ist »unser« Hundeplatz) und
- Berlin,DE -- Geo-Koordinaten [52.5244, 13.4105] (Berlin Mitte)

Per Default kommen die Antwort in Englisch und die Temperaturangaben in Kelvin. Will man sie in Deutsch und °Celsius haben, muß man der URL noch die Parameter `&lang=de` und `&units=metric` mitgeben. Ein Aufruf für Berlin-Tempelhof sähe dann so aus:

~~~
http://api.openweathermap.org/data/2.5/weather?q=Berlin%20Tempelhof,DE&units=metric&lang=de&APPID=0815
~~~

Die APPID habe ich mir ausgedacht, Ihr müßt Euch schon selber eine besorgen (die dann auch viel komplizierter und länger ist). Wird die Anfrage mit einer gültigen APPID abgeschickt, bekommt Ihr eine Antwort der Art:

~~~json
{"coord":
	{"lon":13.41,"lat":52.48},
	"weather":[{"id":500,"main":"Rain","description":"leichter Regen","icon":"10d"}],
	"base":"stations",
	"main":
		{"temp":8,"pressure":992,"humidity":93,"temp_min":8,"temp_max":8
	},
	"visibility":9000,
	"wind":{"speed":5.7,"deg":210},"clouds":{"all":90},
	"dt":1487857800,
	"sys":
		{"type":1,"id":4892,"message":0.0029,"country":"DE","sunrise":1487829867,"sunset":1487867737
	},
	"id":7290253,"name":"Berlin Tempelhof","cod":200
}
~~~

Die Antwort kommt in einer Zeile, ich habe sie nur der besseren Lesbarkeit wegen umgebrochen. Die Bedeutung der einzelnen Paramter bekommt Ihr auf [dieser Seite](http://openweathermap.org/current) erklärt und die *Weather Condition Codes* und Icons sind auf [dieser Seite](http://openweathermap.org/weather-conditions) aufgeführt.

![Screenshot Wetterstation](images/wetterstation.jpg)

## Die Wetterstation mit Processing.py

Um diese JSON-Daten nun mit Processing.py lesen zu können, kann man auf die Standardbibliothek zurückgreifen, die einmal mit `urllib2` einen einfachen Umgang mit dem Laden von Daten aus dem Netz erlaubt und zum anderen mit `json` ein Modul mitbringt, das den Umgang mit den JSON-Dateien vereinfacht.

~~~python
import json
import urllib2
weatherUrl = "http://api.openweathermap.org/data/2.5/weather?q=Berlin%20Tempelhof,DE&units=metric&lang=de&APPID=4711"
weatherData = json.load(urllib2.urlopen(weatherUrl))
~~~

Noch einmal: Den API-Key (`APPID`) habe ich mir ausgedacht, um den Code-Schnipsel oben zum Laufen zu bekommen, müßt Ihr Euch auf den Seiten von OpenWeatherMap schon einen eigenen API-Key besorgen.

~~~pyton
{
    u'visibility': 10000,
    u'main': {
        u'temp': 3,
        u'pressure': 1007,
        u'temp_max': 3,
        u'temp_min': 3,
        u'humidity': 74
    },
    u'clouds': {u'all': 40},
    u'sys': {
        u'country':
        u'DE',
        u'sunrise': 1487916142,
        u'type': 1,
        u'message': 0.0025,
        u'sunset': 1487954244,
        u'id': 4892
    },
    u'dt': 1487940600,
    u'coord': {u'lon': 13.41, u'lat': 52.48},
    u'weather': [{
        u'icon': u'13d', u'description': u'm\xe4\xdfiger Schnee', u'main': u'Snow', u'id': 600
    }],
    u'name': u'Berlin Tempelhof',
    u'cod': 200,
    u'id': 7290253,
    u'base': u'stations',
    u'wind': {u'deg': 310, u'speed': 4.6}
}
~~~

Laßt Ihr Euch die `weatherData` aus obigem Codeschnipsel mal anzeigen (ich habe sie wieder der besseren Lesbarkeit wegen umgebrochen), dann seht Ihr, daß die JSON-Bibliothek die Antwort als *Dictionary* behandelt und Ihr damit nicht mehr auf die Reihenfolge bauen könnt. Es ist zwar alles vorhanden, was Ihr auch ganz oben in der ersten Anwort seht, aber in einer völlig anderen Reihenfolge. Außerdem hat die Bibliothek alle Strings als UTF-8-Strings gekennzeichnet.

Nun lassen sich aber die Werte in *Dictionaries* in Python mit Ihrem Key abfragen und die Keys können miteinander verkettet werden. Wollt Ihr zum Beispiel den Wert des Dictionaries `"temp"`, das Teil des Dictionaries `"main"` ist, abfragen, so ist dies mit

~~~python
temp = weatherData["main"]["temp"]
~~~

möglich. In einigen Fällen beinhalten die JSON-Objekte aber auch Listen. Diese können aber ebenfalls verkettet werden und werden über ihren Index aufgerufen. Wollt Ihr zum Beispiel die Wetterbeschreibung (`"description"`) aus dem Dictionary `"weather"` haben, so müßt Ihr folgendes programmieren:

~~~python
wetter = weatherData["weather"][0]["description"]
~~~

So habe ich mir Stück für Stück alle Daten, die ich für mein kleines Wetterfenster haben wollte, zusammengeklaubt.

Schaut Ihr Euch die Daten, die eine Datums- und Zeitangabe betreffen, genauer an, werdet Ihr feststellen (oder in der Dokumentation nachlesen), daß diese -- wie international üblich -- als UTC-Timestamp kommen. Um dieses zu konvertieren, bildet das Modul `datetime` Hilfe an, zum Beispiel:

~~~python
import datetime
sunrise = weatherData["sys"]["sunrise"]
lokalsunrise = datetime.datetime.fromtimestamp(sunrise).ctime()
~~~

Mit `fromtimestamp` wird der UTC-Stempel in eine lesbare Zeit verwandelt und das anschließende `ctime` sorgt dafür, daß dies in die lokale Rechnerzeit umgewandelt wird (in meinem Fall in UTC+1 oder während der Sommerzeit in UTC+2). Um die Sommerzeit kümmert sich `ctime` automatisch, da muß sich der Programmierer nicht weiter sorgen.

Das Wetter-Icon kommt natürlich auch von OpenWeatherMap und kann so geladen und angezeigt werden:

~~~python
icon = weatherData["weather"][0]["icon"]
weatherIcon = loadImage("http://openweathermap.org/img/w/" + icon + ".png")
image(weatherIcon, 10, 260)
~~~

Das ist eigentlich alles, was der Programmierer wissen muß. Für die aktuelle Zeit habe ich ebenfalls das Modul `datetime` genutzt und die Berechnungen durchgeführt, die ich auch schon in dem Programm zur [Rentenuhr](http://py.kantel-chaos-team.de/rentenuhr/) genutzt hatte.

Um den Hauptsketch übersichtlich zu halten, habe ich die beiden Funktionen `getWeatherData()` und `getNow()` in ein eigenes Modul `getWeatherData.py` ausgelagert, das wie folgt aussieht:

~~~python
# coding=utf-8
import json
import urllib2
import datetime

def getWeatherData():
    weatherUrl = "http://api.openweathermap.org/data/2.5/weather?q=Berlin%20Tempelhof,DE&units=metric&lang=de&APPID=4711"
    weatherData = json.load(urllib2.urlopen(weatherUrl))
    
    # Temperatur
    temp = weatherData["main"]["temp"]
    myTemperatur = u"Temperatur: " + str(temp) + u"°C."
    text(myTemperatur, 10, 20)
    
    # Wetter-Beschreibung
    wetter = weatherData["weather"][0]["description"]
    myWetter = u"Wetter: " + wetter + "."
    text(myWetter, 10, 42)
    
    # Sonnenauf- und -untergang
    sunrise = weatherData["sys"]["sunrise"]
    sunset = weatherData["sys"]["sunset"]
    mySunrise = "Sonnenaufgang: " + datetime.datetime.fromtimestamp(sunrise).ctime() + "."
    mySunset =  "Sonnenuntergang: " + datetime.datetime.fromtimestamp(sunset).ctime() + "."                             
    text(mySunrise, 10, 80)
    text(mySunset, 10, 102)
    
    # Luftdruck und -feuchtigkeit
    pressure = weatherData["main"]["pressure"]
    myPressure = "Luftdruck: " + str(pressure) + " hPa."
    text(myPressure, 10, 140)
    humidity = weatherData["main"]["humidity"]
    myHumidity = "Luftfeuchtigkeit: " + str(humidity) + " %."
    text(myHumidity, 10, 162)
    
    # Windgeschwindigkeit und Bewölkung
    wind = weatherData["wind"]["speed"]
    myWind = "Windgeschwindigkeit: " + str(wind) + " m/s."
    text(myWind, 10, 200)
    clouds = weatherData["clouds"]["all"]
    myClouds = u"Bewölkung: " + str(clouds) + " %."
    text(myClouds, 10, 222)
    
    # Wetter-Icon
    icon = weatherData["weather"][0]["icon"]
    weatherIcon = loadImage("http://openweathermap.org/img/w/" + icon + ".png")
    image(weatherIcon, 10, 260)
    
    # Abfragezeit und -ort
    dt = weatherData["dt"]
    station = weatherData["name"]
    myDt = "Stand: " + datetime.datetime.fromtimestamp(dt).ctime() + " aus " + station + "."
    text(myDt, 10, 360)

def getNow():
    myNow = datetime.datetime.now()
    myHour = str(myNow.hour)
    myMinute = str(myNow.minute).rjust(2, "0")
    mySecond = str(myNow.second).rjust(2, "0")
    myTime = myHour + ":" + myMinute + ":" + mySecond              
    text(u"Update: " + myTime, 10, 382)
~~~

Zum letzten Mal: Die APPID habe ich mir ausgedacht, mit dieser bekommt Ihr keine Daten von OpenWeatherMap.

Das Modul wirkt auf den ersten Blick schlimmer als es ist, denn eigentlich ist alles *straigforward*: Die Daten werden aus dem JSON-Objekt ausgelesen, dann wird ein String erzeugt und zum Schluß wird dieser String mit Hilfe der `text()`-Funktion angezeigt.

So ist das Hauptprogramm wieder sehr kurz geraten:

~~~python
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
~~~

In der `setup()`-Funktion rufe ich zu Initialisierung genau einmal die Wetterdaten ab. Nun darf man in der kostenlosen Lizenz die Daten maximal 60 mal in der Minute abrufen. Mit `frameRate(1)` alleine schafft man das nicht (ich habe sie auch nur darauf gesetzt, um den Rechner nicht unnötig zu belasten). Darum werden die weiteren Abfragen nur gestartet, wenn die Sekunde auf Null steht, das heißt es gibt nur einen Aufruf in der Minute. Damit habe ich die Lizenz der API mehr als eingehalten.

Eigentlich könnte man die Daten noch seltener abrufen: Die von mir angefragte Station *Berlin Tempelhof* gibt nur jede halbe Stunde (um x:20 Uhr und um x:50 Uhr) ihre Daten weiter und es kann noch bis zu einer weiteren halben Stunde dauern, bis die Daten bei OpenWeatherMap eingepflegt und abrufbar sind. Im schlimmsten Fall kann es zu Verzögerungen bis zu einer Stunde kommen, manchmal sind die neuen Daten aber auch überraschend schnell da.

Sicher kann man die Wetterstation optisch noch ein wenig aufpeppen und man kann auch mehrere Wetterstationen abfragen oder die API zur Wettervorhersage nutzen, aber als Beispiel, wie man JSON-Daten per API aus dem Netz holt und aufbereitet, ist dieser Sketch völlig ausreichend. Alles weitere bleibt der Phantasie meiner Leserinnen und Leser überlassen.