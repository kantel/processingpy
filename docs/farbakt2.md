# Noch mehr Pointillismus

Wenn ich ehrlich bin, kann das Ergebnis des Programms aus dem letzten Abschnitt weder ästhetisch noch im Sinne des Pointillismus wirklich überzeugen. Das liegt daran, daß im Programm jedes einzelne Pixel befragt und dann als vergrößerter Punkt wiedergegeben wird. So entsteht im Endeffekt so etwas wie ein verwaschenes Original, aber kein Raster. Daher habe ich -- nach einer Idee aus dem wunderbaren Buch »[Generative Gestaltung][amazon1]« (derzeit leider nur auf englisch [verfügbar][amazon2]) -- tatsächlich eine Rasterversion des Aktbildes programmiert und das Ergebnis überzeugt mich mehr:

[![Screenshot](images/akt2.jpg)](https://www.flickr.com/photos/schockwellenreiter/34807667812/)

Dafür habe ich zuerst das Bild, das im Original 400 x 640 Pixel groß war, auf 50 x 80 Pixel verkleinert um dann mit

~~~python
tileWidth = width/float(akt.width)
tileHeight = height/float(akt.height)
posX = tileWidth*gridX
posY = tileHeight*gridY
~~~

ein entsprechendes Raster für das immer noch 400 x 640 Pixel große Ausgabefenster zu schaffen. Mit der Formel

~~~python
greyscale = round(red(cc)*0.222 + green(cc)*0.707 + blue(cc)*0.071)
~~~

habe ich danach die abgetasteten Farben in Graustufen gewandelt, die Gewichtungen habe ich dem oben erwähnten Buch »Generative Gestaltung« entnommen, die [Wikipedia](https://de.wikipedia.org/wiki/Grauwert) zum Beispiel nennt andere Gewichtungen, aber auch gleichverteilte Gewichtungen sind möglich und üblich. Hier gibt es also noch Raum für Experimente.

Mit

~~~python
w = map(greyscale, 0, 255, 12, 0)
~~~

habe ich dann den Radius der Kreise in Abhängigkeit von der Graustufe bestimmt: Je dunkler die Graustufe, desto größer der Kreis. Den Wert `12` habe ich experimentell herausgefunden, auch hier ist ebenfalls noch Raum für Experimente. So bekommt man zum Beispiel auch ein nettes Ergebnis, wenn man die Zeile

~~~python
fill(cc)
~~~

durch

~~~python
fill(greyscale)
~~~

ersetzt. Der [Processing-Quellcode](https://github.com/generative-design/Code-Package-Processing-3.x/blob/master/01_P/P_4_3_1_01/P_4_3_1_01.pde) aus »Generative Gestaltung« zeigt ebenfalls noch ein paar wirklich nette Möglichkeiten, was man mit so einem Grid alles anstellen kann.

## Der Quellcode

Hier nun der vollständige Quellcode, er ist -- wie fast immer -- erfrischend kurz:

~~~python
def setup():
    global akt
    size(400, 640)
    akt = loadImage("akt50x80.jpg")
    background(255)
    noLoop()

def draw():
    global akt
    for gridX in range(akt.width):
        for gridY in range(akt.height):
            # grid position and tile size
            tileWidth = width/float(akt.width)
            tileHeight = height/float(akt.height)
            posX = tileWidth*gridX
            posY = tileHeight*gridY
            # get current color
            cc = akt.pixels[gridY*akt.width + gridX]
            # greyscale conversion
            greyscale = round(red(cc)*0.222 + green(cc)*0.707 + blue(cc)*0.071)
            # pixel color to fill, greyscale to ellipse size
            noStroke()
            fill(cc)
            w = map(greyscale, 0, 255, 12, 0)
            ellipse(posX, posY, w, w)
~~~





[amazon1]: https://www.amazon.de/Generative-Gestaltung-Programmieren-internationalen-Best-Practise-Beispielen/dp/3874397599/ref=as_li_ss_tl?ie=UTF8&qid=1496078767&sr=8-1&keywords=Generative+Gestaltung&linkCode=ll1&tag=derschockwell-21&linkId=006bf37e45fc0b671a7ec6a217fb69da
[amazon2]: https://www.amazon.de/Generative-Design-Visualize-Program-Processing/dp/1616890770/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=derschockwell-21&linkId=60caedf2804bda621d07eea10332003d