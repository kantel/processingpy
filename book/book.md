---
title: Processing.py in Beispielen
subtitle: Visualisierungen und interaktive Anwendungen mit Python und Processing programmieren
author: Jörg Kantel
date: \today
---


# Einleitung

# Download und Installation

# Start: Rotkäppchen und die drei Tanten

Rotkäppchen hat nicht nur eine Großmutter, sondern -- was weniger bekannt ist -- auch drei Tanten, Agathe, Beatrice und Cynthia. Diese wohnen in drei Häusern, die zusammen ein Dreieck bilden. Wenn Rotkäppchen nicht ihre Großmutter besucht, dann besucht sie eine der drei Tanten. Letzten Sonntag jedoch war sie sehr unschlüssig, welche sie besuchen sollte. Sie startete, um Agathe einen Besuch abzustatten. Jedoch genau auf dem halben Weg zu Agathe wurde sie unsicher und überlegte es sich noch einmal. Sie beschloß, eine ihrer drei Tanten aufzusuchen, es könnte auch wieder Agathe gewesen sein. Doch es war wie verhext: Jedesmal, wenn sie genau den halben Weg zurückgelegt hatte, wurde sie wieder unsicher und entschloß sich neu, einer ihrer drei Tanten aufzusuchen, möglicherweise die gleiche, möglicherweise eine andere. Und das wieder, und wieder, und wieder …

[![Screenshot](images/sierpinskidreieck.jpg)](https://www.flickr.com/photos/schockwellenreiter/32442344526/)

*William P. Beuamont* [Beaum1996] nannte es das »Tantenspiel«. Ziel ist es nicht, herauszufinden, welche Tante gewinnt (es kann gar keine gewinnen), sondern welche Figur entsteht, wenn man Rotkäppchens Irrweg visualisiert. Ich habe das einmal mit Processing.py nachprogrammiert und herausgekommen ist obige Figur, in der Fachliteratur auch als [Sierpinski Dreieck][3_1] bekannt, benannt nach dem polnischen Mathematiker *Wacław Sierpiński*, der das Fraktal schon 1915 als erster beschrieb.

[3_1]: https://de.wikipedia.org/wiki/Sierpinski-Dreieck


## Der Quellcode

Normalerweise wird dieses Fraktal mit einem rekursiven Algorithmus erzeugt, aber es geht eben auch mithilfe dieses »Chaos-Spiels« [Herrm1994]

~~~python
import random as r

i = 0
x = y = 0

def setup():
    size(640, 480)
    background(0)
    colorMode(HSB, 360, 100, 100)
    frameRate(1200)

def draw():
    global i, x, y
    p = r.randint(0, 2)
    if (p == 0):
        x /= 2
        y = (y + 480)/2
    elif (p == 1):
        x = (x + 320)/2
        y /= 2
    else:
        x = (x + 640)/2
        y = (y + 480)/2
    stroke(i%360, 100, 100)
    point(x, y)
    i += 1
    if (i > 120000):
        print("I did it, Babe!")
        noLoop()
~~~

Die Schleife wird 120.000 mal durchlaufen, bevor sie stoppt. Damit ich nicht ewig auf das Ergebnis warten muß, habe ich die Framerate auf 1.200 FPS gesetzt. Das ist vermutlich etwas übertrieben, in diversen Foren habe ich Vermutung gefunden, daß Processing kaum eine Framerate von 1.000 FPS überschreiten kann. Das habe ich experimentell bestätigt, obiger Sketch lief auf meinem schnellsten Rechner, einem Mac Pro mit 3,5 GHz 6-Core Intel Xeon E5, 2 Minuten und 20 Sekunden. Wären genau 1.000 FPS erreicht worden, hätte er exakt 2 Minuten laufen müssen.

Aber man sieht sehr schön, wie sich das Dreieck zufällig, aber dennoch erkennbar, zusammensetzt. Je nach zufälligem Startwert liegen die ersten drei bis vier Punkte noch außerhalb des Fraktals, danach geht aber alles seinen geordneten Gang. Und an den Farben erkennt man, daß auch die Reihenfolge, in der die einzelnen Punkte des Fraktals von Rotkäppchen angelaufen werden, ebenfalls zufällig sind.



## Literatur

- *[Beaum1996]* William P. Beaumont: *Conquering the Math Bogeyman*, in Clifford A. Pickover (Ed.): *Fractal Horizons -- The Future Use of Fractals*, New York (St. Martin's Press) 1996, Seiten 3 - 15
- *[Herrm1994]* Dietmar Herrmann: *Algorithmen für Chaos und Fraktale*, Bonn (Addison-Wesley) 1994, Seiten 132ff.

# Punkte und Pixel

## Turmite

Turmiten sind quadratische, 1x1 Pixel große, kybernetische Kreaturen mit einer höchst kümmerlichen Andeutung eines Gehirns. Sie können die Farben des Pixels oder der Zelle, auf der sie gerade stehen, erkennen und danach handeln. Ist die Zelle schwarz, färben sie sie rot und bewegen sich um ein Feld nach links. Ist die Farbe rot, färben sie die Zelle schwarz und bewegen sich um ein Feld nach rechts.

![Die Turmite in Aktion](images/turmite.jpg)

Wird solch eine Turmite auf eine schwarze, unendlichen Ebene gesetzt, erzeugt sie zuerst ein chaotisches Muster. Doch nach ungefähr 10.000 Schritten bildet sie auf einmal eine Turmiten-Autobahn, eine regelmäßige Struktur, die immer nach 104 Schritten in denselben Zustand zurückkehrt, nur jeweils um 2 Felder verschoben.

### Die Turmite programmieren

Ich habe eine dieser Turmiten in einem Processing.py-Sketch zum Leben erweckt. Damit sie nicht in der Unendlichkeit der Ebene entfleucht, habe ich die Ecken des Fensters miteinander verklebt und sie so in eine [Torus](https://de.wikipedia.org/wiki/Torus)-Welt verwandelt. Wenn die Turmite am unteren Ende des Fensters verschwindet, taucht sie am oberen Ende wieder auf, verschwindet sie am rechten Rand erscheint sie wieder am linken Rand. Für beide Ränder gilt das natürlich auch umgekehrt, die Welt der Turmite ist also ein fett aufgeblasener Fahrradschlauch, auf dem sie sich entlang bewegt.

Den Farbsensor der Turmite habe ich mit dem Processing-Befehl `get(x, y)` simuliert. Er liest die Farbe des Pixels. Analog dazu gibt es die Funktion `set(x, y, color)`, die die Farbe `color` an die Stelle `x, y` schreibt. Die beiden Farben habe ich im Sketch `on` für schwarz und `off` für rot genannt. Ich bin von der Metapher ausgegangen, daß die Turmite auf der schwarzen Ebene ein Feld entweder einschaltet (also rot färbt) oder es wieder ausschaltet (es wird wieder schwarz).

Als ich damals auf meinem Atari-ST mein erstes Turmitenprogramm schrieb, dauerte es ewig, bis die Turmite mit ihrer Autobahn im Unendlichen verschwunden war (sie das Bildschirmfenster verlassen hatte). An eine Rückkehr via Torus wagte ich nicht zu denken, dafür reichte meine Geduld nicht aus. Nun in Processing.py habe ich die Framerate auf 600 gesetzt und so geht es doch recht schnell voran.

Interessant ist, daß die Turmite, wenn sie auf eine von ihr geschaffene Autobahn trifft, zwar erst einmal wieder ein chaotisches Verhalten an den Tag legt, aber über kurz oder lang wieder eine Autobahn baut. Diese Turmiten-Autobahnen kennen nur zwei Orientierungen, sie verlaufen entweder parallel oder stehen senkrecht aufeinander.

### Quellcode

Nach dem oben Beschriebenen dürfte der Quellcode leicht verständlich sein. In der `setup()`-Funktion wird die Hintergrundfarbe auf schwarz und die Turmite in die Mitte des Fensters mit der Ausrichtung nach Norden gesetzt.

Im ersten Abschnitt der `draw()`-Funktion wird die Turmite gemäß Ihrer aktuellen Orientierung bewegt und die Behandlung der Fensterränder berücksichtigt. Dann wird die Farbe der aktuellen Zelle gelesen (mit `get(x, y)`) und je nach Zustand eine neue Farbe gesetzt und die Orientierung der Turmite den Regeln entsprechend geändert. Das ist alles.

~~~python
south = 0
east  = 1
north = 2
west  = 3

on  = color(188, 0, 0)   # rot
off = color(0)           # schwarz

def setup():
    global x, y, dir
    size(600, 200)
    x = width/2
    y = height/2
    dir = north
    background(0)
    frameRate(600)

def draw():
    global x, y, dir
    if (dir == south):
        y += 1
        if (y == height):
            y = 0
    elif (dir == east):
        x += 1
        if (x == width):
            x = 0
    elif (dir == north):
        if (y == 0):
            y = height - 1
        else:
            y -= 1
    elif (dir == west):
        if (x == 0):
            x = width - 1
        else:
            x -= 1
    
    if (get(x, y) == on):
        set(x, y, off)
        if (dir == south):
            dir = west
        else:
            dir -= 1
    else:
        set(x, y, on)
        if (dir == west):
            dir = south
        else:
            dir += 1
~~~

### Weitere mögliche Experimente

Die Turmiten gehen auf *Greg Turk* zurück, der damals Doktorand an der Universität von North Carolina in Chapel Hill war. Er zeigte, daß sie eine zweidimensionale [Turingmaschine](https://de.wikipedia.org/wiki/Turingmaschine) sind. Später hat sie *Christopher Langton* weiterentwickelt und beschrieben -- daher ist sie auch unter dem Namen »Langtons Ameise« *(Lanton's Ant)* bekannt. Die hier vorgestellte ist die einfachste Form solch einer Ameise. Ein nächster Schritt wäre beispielsweise, die Welt mit zwei Turmiten zu bevölkern, die eine färbt die Ebene rot, wenn sie auf ein schwarzes Feld trifft, die andere färbt sie blau. Natürlich müßten dann beide Ameisen auch Regeln implementiert bekommen, wie sie zu verfahren haben, wenn sie auf ein blaues respektive ein rotes Feld treffen.

Von Turk selber gibt es zum Beispiel eine Turmite mit zwei Zuständen, nennen wir diese `A` und `B` und mit folgendem Regelsatz:

Zustand  | A                   | B
:--------|:--------------------|:--------------
grün     | schwarz, vorwärs, B | grün, rechts, A
schwarz  | grün, links, A      | grün, rechts, A

Sie erzeugt ein Spiralmuster, »immer größer werdende strukturierte Gebiete, die sich in regelmäßiger Anordnung um einen Startpunkt winden«.

Eine weitere Turmite, die mit vier Farben hantiert, braucht nur einen Zustand, um ebenfalls ein interessantes, symmetrisches Muster zu bilden. Hier ihr Regelsatz:

Zustand | A
:-------|:---------
blau    | rot, rechts, A
rot     | gelb, rechts, A
gelb    | grün, links, A
grün    | blau, links, A

Es gibt also noch viel zu entdecken in der Welt der Turmiten und Ameisen.

### Literatur

- A.K. Dewdney: *Turmiten*, in: Immo Diener (Hg.): *Computer-Kurzweil 2, Spektrum Akademischer Verlag: Verständliche Forschung*, Heidelberg 1992, Seiten 156-160
- [Ameise (Turingmaschine)](https://de.wikipedia.org/wiki/Ameise_(Turingmaschine)) in der Wikipedia.

## Wir backen uns ein Mandelbrötchen

![Die Mandelbrotmenge](images/mandelbrotmenge.jpg)

Die [Mandelbrot-Menge](https://de.wikipedia.org/wiki/Mandelbrot-Menge) ist die zentrale Ikone der Chaos-Theorie und das Urbild aller Fraktale. Sie ist die Menge aller komplexen Zahlen *c*, für welche die durch


\begin{align}
z_{0} & = 0\\
z_{n+1} & = z_{n}^{2}+c
\end{align}



rekursiv definierte Folge beschränkt ist. Bilder der Mandelbrot-Menge können erzeugt werden, indem für jeden Wert des Parameters *c*, der gemäß obiger Rekursion endlich bleibt, ein Farbwert in der komplexen Ebene zugeordnet wird.

Die komplexe Ebene wird in der Regel so dargestellt, daß in der Horizontalen (in der kartesisschen Ebene die *x-Achse*) der Realteil der komplexen Zahl und in der Vertikalen (in der kartesischen Ebene die *y-Achse*) der imaginäre Teil aufgetragen wird. Jede komplexe Zahl entspricht also einen Punkt in der komplexen Ebene. Die zur Mandelbrotmenge gehörenden Zahlen werden im Allgemeinen schwarz dargestellt, die übrigen Farbwerte werden der Anzahl von Iterationen (`maxiter`) zugeordnet, nach der der gewählte Punkt der Ebene einen Grenzwert (`maxlimit`) verläßt. Der theoretische Grenzwert ist *2.0*, doch können besonders bei Ausschnitten aus der Menge, um andere Farbkombinationen zu erreichen, auch höhere Grenzwerte verwendet werden. Bei Ausschnitten muß auch die Anzahl der Iterationen massiv erhöht werden, um eine hinreichende Genauigkeit der Darstellung zu erreichen.

### Das Programm

Python kennt den Datentyp `complex` und kann mit komplexen Zahlen rechnen. Daher drängt sich die Sprache für Experimente mit komplexen Zahlen geradezu auf. Zuert werden mit `cr` und `ci` Real- und Imaginärteil definiert und dann mit

~~~python
c = complex(cr, ci)
~~~

die komplexe Zahl erzeugt. Für die eigentliche Iteration wird dann -- nachdem der Startwert `z = 0.0` festgelegt wurde -- nur eine Zeile benötigt:

~~~python
z = (z**2) + c
~~~

Wie schon in anderen Beispielen habe ich für die Farbdarstellung den HSB-Raum verwendet und über den *Hue*-Wert iteriert. Das macht alles schön bunt, aber es gibt natürlich viele Möglichkeiten, ansprechendere Farben zu bekommen, beliebt sind zum Beispiel selbsterstellte Paletten mit 256 ausgesuchten Farbwerten, die entweder harmonisch ineinander übergehen oder bestimmte Kontraste betonen.

### Der komplette Quellcode

~~~python
left   = -2.25
right  = 0.75
bottom = -1.5
top    = 1.5
maxlimit = 2.0
maxiter = 20

def setup():
    size(400, 400)
    background("#ffffff")
    colorMode(HSB, 255, 100, 100)
    noLoop()

def draw():
    for x in range(width):
        cr = left + x*(right - left)/width
        for y in range(height):
            ci = bottom + y*(top - bottom)/height
            c = complex(cr, ci)
            z = 0.0
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    set(x, y, color(0, 0, 0))
                else:
                    set(x, y, color((i*48)%255, 100, 100))
~~~

Um zu sehen, wie sich die Farben ändern, kann man durchaus mal mit den Werten von `maxlimit` spielen und diesen zum Beispiel auf `3.0` oder `4.0` setzen. Auch die Erhöhung der Anzahl der Iterationen `maxiter` verändert die Farbzuordnung, verlängert aber auch die Rechhenzeit drastisch, so daß man speziell bei Ausschnitten aus der Mandelbrotmenge schon einige Zeit auf das Ergebnis warten muß.

## Pixel-Array versus set()

Will man einzelne Pixel im Ausgabefenster oder in einem Bild manipulieren, bietet Processing(.py) grundsätzlich zwei Möglichkeiten: Zum einen kann man mit

~~~python
set(x, y, color)
~~~

direkt einen Farbpunkt an eine bestimmte Position `x, y` setzen, oder aber man lädt mit

~~~python
loadPixels()
~~~

das gesamte Ausgabe-Fenster in ein eindimensionales Pixel-Array, um dann mit

~~~python
pixels[x + y*width] = color()
~~~

die Farbe an die gewünschte Stelle `x, y` zu setzen. Anschließend darf man nicht vergessen, mit

~~~python
updatePixels()
~~~

Processing dazu zu bewegen, die geänderten Pixel auch anzuzeigen. Dadurch, daß das Pixel-Array eindimensional ist und so die gewünschte Position mit `x + y*width` angesprochen werden muß, ist die erste Version (für die es übrigens auch noch ein entsprechendes `get(x, y)` gibt, mit dem man die Farbe an der gewünschten Stelle abfragen kann) einfacher handzuhaben, aber die [Reference zu Processing](https://processing.org/reference/set_.html) zu bedenken:

>Setting the color of a single pixel with set(x, y) is easy, but not as fast as putting the data directly into pixels[].

Das gilt aber nicht immer, mit dem im [letzten Abschnitt gebackenen Mandelbrötchen](mandelbrot.md) habe ich die Probe aufs Exempel gemacht. Zwei nahezu identische Programme habe ich gegeneinander antreten lassen.

### Programm 1: Mandelbrot-Menge mit set()

~~~python
left   = -2.25
right  = 0.75
bottom = -1.5
top    = 1.5
maxlimit = 4.0
maxiter = 100

def setup():
    size(600, 600)
    background("#ffffff")
    colorMode(HSB, 255, 100, 100)
    noLoop()

def draw():
    for x in range(width):
        cr = left + x*(right - left)/width
        for y in range(height):
            ci = bottom + y*(top - bottom)/height
            c = complex(cr, ci)
            z = complex(0.0, 0.0)
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    set(x, y, color(0, 0, 0))
                else:
                    set(x, y, color((i*48)%255, 100, 100))
    println(millis())
~~~

### Programm 2: Mandelbrot-Menge mit Pixel-Array

~~~python
left   = -2.25
right  = 0.75
bottom = -1.5
top    = 1.5
maxlimit = 4.0
maxiter = 100

def setup():
    size(600, 600)
    background("#ffffff")
    colorMode(HSB, 255, 100, 100)
    noLoop()

def draw():
    loadPixels()
    for x in range(width):
        cr = left + x*(right - left)/width
        for y in range(height):
            ci = bottom + y*(top - bottom)/height
            c = complex(cr, ci)
            z = complex(0.0, 0.0)
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    pixels[x + y*width] = color(0, 0, 0)
                else:
                    pixels[x + y*width] = color((i*48)%255, 100, 100)
    updatePixels()
    println(millis())
~~~

Und -- Überraschung! -- das Programm mit `set()` war fast immer geringfügig schneller als das Programm mit den Pixel-Arrays. Auf meinem betagten MacBook Pro benötigte das erste Programm rund 15.000 bis 16.000 Millisekunden, während das zweite Programm um die 18.000 Millisekunden benötigte. Der Unterschied ist nicht groß, aber dennoch bemerkenswert. Es liegt zum einen sicher daran, daß die benötigte Zeit für die Berechnung des Apfelmännchens im Vergleich zu der benötigten Zeit, dieses zu zeichnen, riesig ist. Zum anderen wird die `draw()`-Schleife ja auch nur einmal durchlaufen und so kann das Pixel-Array seine Fähigkeit der schnellen Pixelmanipulation nicht richtig ausspielen.

Die Erkenntnis daraus: Es kann sich durchaus lohnen, auch mal das Handbuch zu hinterfragen. 😈

## Julia-Menge

![Screenshot](images/julia.jpg)

Die [Julia-Menge](https://de.wikipedia.org/wiki/Julia-Menge) wurde 1918 von den beiden französischen Mathematikern *Gaston Maurice Julia* (nachdem sie benannt wurde) und *Pierre Fatou* (dessen Zugang heute die meisten Lehrbücher folgen) unabhängig voneinander beschrieben. Sie steht im engen Zusammenhang zur im letzten Abschnitt beschriebenen [Mandelbrot-Menge](mandelbrot.md). Während die Mandelbrot-Menge, die Menge aller komplexen Zahlen *c* ist, die der iterierten Gleichung


\begin{align}
z_{0} & = 0\\
z_{n+1} & = z_{n}^{2}+c
\end{align}

folgen, ist bei der Julia-Menge *c* konstant:


\begin{align}
z_{n}^{2}+c
\end{align}


Die Mandelbrot-Menge ist also eine Beschreibungsmenge aller Julia-Mengen. Jedem Punkt *c* der komplexen Zahlenebene entspricht eine Julia-Menge. Eigenschaften der Julia-Menge lassen sich an der Lage von *c* relativ zur Mandelbrot-Menge beurteilen: Wenn der Punkt *c* Element der Mandelbrot-Menge ist, dann ist die Julia-Menge zusammenhängend. Andernfalls ist sie eine Cantormenge unzusammenhängender Punkte. Ist der Imaginärteil *c<sub>i</sub> = 0*, dann ist die Julia-Menge symmetrisch (vlg. Abbildung links oben), ansonsten kann sie alle möglichen Formen annehmen.

### Julia-Menge interaktiv

Ich habe die obigen Bilder mit diesem Programm erzeugt, daß den Parameter *c* in Abhängigkeit von der Mausposition setzt:

~~~python
left   = -2.0
right  = 2.0
bottom = 2.0
top    = -2.0
maxlimit = 3.0
maxiter = 25

def setup():
    size(400, 400)
    background("#555ddd")
    colorMode(HSB, 1)

def draw():
    cr = map(mouseX, 0, width, left, right)
    ci = 0
    # ci = map(mouseY, 0, height, top, bottom)
    c = complex(cr, ci)
    for x in range(width):
        zr = left + x*(right - left)/width
        for y in range(height):
            zi = bottom + y*(top - bottom)/height
            z = complex(zr, zi)
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter-1):
                    set(x, y, color(0))
                else:
                    set(x, y, color(sqrt(float(i)/maxiter), 100, 100))
    println("cr = " + str(cr))
    println("ci = " + str(ci))
~~~

Kommentiert man die Zeile `ci = 0` aus und aktiviert stattdessen die auskommentierte Zeile darunter, erhält man (theoretisch) alle Julia-Mengen, sonst erzeugt das Programm nur die symmetrischen. Richtig flüssig ist die Animation allerdings nicht, Processing.py gerät -- zumindest auf meinem betagten MacBook Pro -- schon ganz schön ins Stottern.

### Julia-Menge animiert

Das gilt auch für das zweite Programm, das die Parameter der Julia-Menge anhand zweier Sinus- (wahlweise auch Cosinus-) Funktionen periodisch durchläuft:

~~~python
left   = -2.0
right  = 2.0
bottom = 2.0
top    = -2.0
maxlimit = 3.0
maxiter = 25

def setup():
    size(400, 400)
    background("#555ddd")
    colorMode(HSB, 1)

def draw():
    # cr = 0
    cr = 2*sin(frameCount)
    ci = 0
    # ci = 2*cos(frameCount)
    c = complex(cr, ci)
    for x in range(width):
        zr = left + x*(right - left)/width
        for y in range(height):
            zi = bottom + y*(top - bottom)/height
            z = complex(zr, zi)
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter-1):
                    set(x, y, color(0))
                else:
                    set(x, y, color(sqrt(float(i)/maxiter), 100, 100))
    println("cr = " + str(cr))
    println("ci = " + str(ci))
~~~

Auch hier kommt das Programm ganz schön ins Schwitzen. Das läßt allerdings dem Betrachter Zeit, die Schönheit der Julia-Menge zu bewundern. 

## Schnelle Bildmanipulation: Das Pixel-Array

In den letzten beiden Abschnitt habe ich gezeigt, daß Processing.py zwar relativ schnell ist, aber 120.000 Operationen in einem Bildfenster doch eine gewisse Zeit benötigen. Falls man jedoch auf die Animation verzichten kann (und damit auf `point()` oder `get()` und `set()`), geht es auch wesentlich schneller: Jedes Bild in Processing(.py) -- und das schließt das Graphikfenster ein -- wird intern als eine eindimensionale Liste der Farbwerte gespeichert. Die erste Position der Liste ist das erste Pixel links oben, die letzte Position folgerichtig das letzte Pixel rechts unten.

Ein `pixels[]`-Array in Processing speichert in dieser Form die Farbwerte für jedes Pixels des Ausgabefensters. Um es zu initialisieren, muß vor der ersten Nutzung die Funktion `loadPixels()` aufgerufen werden. Manipulationen im Pixel-Array werden erst sichtbar, wenn die Funktion `updatePixels()` aufgerufen wird. `loadPixels()` und `updatePixels()` bilden so ein ähnliches Geschwisterpaar von Funktionen, wie zum Beispiel `beginShape()` und `endShape()`. Doch einen Unterschied gibt es: Wird das Pixel-Array nur zum Lesen der Farbwerte genutzt, muß `updatePixels()` natürlich nicht aufgerufen werden. Da die Manipulationen eines Pixel-Arrays nur im Hauptspeicher des Rechners stattfinden, sind sie natürlich viel schneller als jede andere Processing-Funktion, die Bildinformationen manipuliert.

Da das Pixel-Array ein eindimensionales Array ist, muß auf die Zeilen und Spalten mit einem kleinen Trick zugegriffen werden. Jeder Punkt `(x, y)` steht im Pixelarray an der Position `x + (y*width)`. An die Farbwerte eines Pixels kommt man mit dem Aufruf

~~~python
i = x + (y*width)
color(c) = pixels[i]
~~~

Die einzelnen Farbwerte im RGB-Raum kann man danach so auslesen:

~~~python
r = red(c)
g = green(c)
b = blue(c)
~~~

Das Setzen eines Pixels erfolgt genau umgekehrt:

~~~python
pixel[i] = color(r, g, b)
~~~

Natürlich kann man auch jeden anderen Farbraum (Graustufen, HSV), den Processing kennt, nutzen.


### Fantastic Feather Fractal

Um zu zeigen, wie schnell die Manipulationen eines Pixel-Arrays sind, möchte ich wieder eine Iteration über 120.000 Schritte durchführen. Als Demonstrationsobjekt habe ich das *Fantastic Feather Fractal* gewählt, das *Clifford A. Pickover* in seinem Buch »Mazes for the Mind« vorgestellt hat. Wenn Ihr untenstehenden Quellcode laufen laßt, werdet Ihr feststellen, daß das fertige Fraktal fast unmittelbar nach dem Aufruf im Graphikfenster erscheint.[^4_1]

[^4_1]: Ich habe das Bild testweise auch mal erst nach 240.000 Schritten herausschreiben lassen. Die Verzögerung war kaum merkbar. Allerdings gab es auch nur noch einen geringen Unterschied zu dem Bild im Screenshot. Hier setzt die Auflösung des Ausgabefensters weiterem Erkenntnisgewinn Grenzen.

[![Feather Fractal](images/featherfractal.jpg)](https://www.flickr.com/photos/schockwellenreiter/32766476595/)

Das *Feather Fractal* ist ein »[seltsamer Attraktor](https://de.wikipedia.org/wiki/Seltsamer_Attraktor)«, ein [Attraktor](http://www.spektrum.de/lexikon/physik/attraktor/926) eines dynamischen Systems, das sich zwar chaotisch verhält, aber dennoch eine *kompakte Menge* ist, die es nie verläßt. Die Parameter des Sketches entstammen der oben genannten Quelle von *Pickover*, die Faktoren um das Ergebnis dem Bildfenster anzupassen habe ich durch wildes Herumexperimentieren gefunden[^4_2].

[^4_2]: Und das schon vor langer Zeit, als der Monitor meines Rechners noch eine Auflösung von 640 x 480 Pixeln hatte. 😜

### Der Quellcode

~~~python
a = -.48
b = .93

def setup():
    size(640, 480)
    background(0)
    colorMode(HSB, 255, 100, 100)
    frame.setTitle("Fantastic Feather Fractal")
    noLoop()

def draw():
    loadPixels()
    x = 4.0
    y = .0
    for i in range(1, 120000, 1):
        x1 = b*y + f(x)
        y = -x + f(x1)
        x = x1
        pixels[(350 + int(x*26)) + ((280 - int(y*26))*width)] = color(i%255, 100, 100)
    updatePixels()

def f(x):
    return a*x - (1.0 - a)*((2*(x**2))/(1.0 + x**2))
~~~

Wenn ich später noch auf Bildmanipulationen in Processing zurückkomme, werden die Pixel-Arrays noch einmal ausführlich behandelt werden.

### Literatur

- Clifford A. Pickover: *Mazes for the Mind. Computer s and the Unexpected*, New York (St. Martin's Press) 1992. Das Buch gehört zu den Besten des umtriebigen Autors und da es aufgrund seines Alters antiquarisch für ein paar Cent zu bekommen ist, solltet Ihr zuschlagen. Das Feder-Fraktal ist auf den Seiten 33f. beschrieben, die über 400 anderen Seiten erfüllen fast jeden Traum eines an Computer-Experimenten interessierten Menschen.
- Florian Freistetter: *[Best of Chaos: Der seltsame Attraktor](http://scienceblogs.de/astrodicticum-simplex/2015/02/04/best-of-chaos-der-seltsame-attraktor/)*, Science Blogs (Astrodicticum Simplex) vom 4. Februar 2015 (Ich bin ein Fan von *Florian Freistetter*, er ist einer der wenigen guten deutschsprachigen Erklärbären für Naturwissenschaften)

# Linien

## Anschauliche Mathematik: Die Schmetterlingskurve

![Schmetterling](images/buttfly.jpg)

Seit ich Ende der 1980er Jahre mit meinem damals hochmodernen [Atari Mega&nbsp;ST](https://de.wikipedia.org/wiki/Atari_ST) erste Schritte mit einem graphikfähigen Personalcomputer unternommen hatte, habe ich die Schmetterlingskurve immer wieder als Test für die Graphikfähigkeit und Schnelligkeit von Programmiersprachen und Rechnern benutzt. Sie wird in [Polarkoordinaten](https://de.wikipedia.org/wiki/Polarkoordinaten) beschrieben und ihre Formel ist

\begin{align}
\rho=e^{\cos(\theta)}-2\cdot \cos(4\cdot \theta)+\sin(\tfrac{\theta}{12})^5
\end{align}


oder in Python-Code:

~~~python
r = exp(cos(theta)) - 2*cos(4*theta) + (sin(theta/12))**5
~~~

Die Gleichung ist hinreichend kompliziert um selbst in C geschriebene Routinen auf meinen damals unglaubliche 8 MegaBit schnellen Atari alt aussehen zu lassen. Rechenzeiten von 10 - 20 Minuten waren keine Seltenheit. Heute dagegen muß man den Rechner schon künstlich verlangsamen, damit man sieht, wie sich die Kurve aufbaut. Denn sonst erscheint sofort die fertige Kurve, um die sinnliche Erfahrung, wie diese entsteht, wird man betrogen. Daher habe ich sie in *Processing.py* innerhalb der `draw()`-Schleife zeichnen lassen, wobei die Schleifenvariable `theta` bei jedem Durchlauf um `0.02` erhöht wurde.

Der Code ist -- dank Processing.py -- wieder von erfrischender Einfachheit und Kürze:

~~~python
def setup():
    global theta, xOld, yOld
    theta = xOld = yOld = 0.0
    size(600, 600)
    background(100, 100, 100)
    colorMode(HSB, 100)
    
def draw():
    global theta, xOld, yOld
    strokeWeight(2)
    stroke(theta, 100 - theta, 100)
    r = exp(cos(theta)) - 2*cos(4*theta) + (sin(theta/12))**5
    # aus Polarkoordinaten konvertieren
    x = r*cos(theta)
    y = r*sin(theta)
    # auf Fenstergröße skalieren
    xx = (x*60) + 300
    yy = (y*60) + 300
    if (theta == 0.0):
        point(xx, yy)
    else:
        line(xOld, yOld, xx, yy)
    xOld = xx
    yOld = yy
    theta += 0.02
    if (theta > 75.39):
        print("I did it, Babe!")
        noLoop()
~~~

In `setup()` ist eigentlich nur bemerkenswert, daß ich nach der Festlegung des grauen Hintergrunds (noch als RGB), den `colorMode` auf HSB geändert habe. Damit lassen sich nämlich recht einfach diverse Farbeffekte erzielen. Ich habe dabei den *Hue*-Wert in Abhängigkeit von `theta` gesetzt, die Sättigung auf `100 - theta` und die *Brightness* konstant bei 100 belassen. Da `theta` nie größer als $75,39$ wird, wird es also auch nie größer als 100 und damit sind diese Umrechnungen gefahrlos.

Damit erreicht man, daß zu Beginn, wo die Sättigung noch ziemlich voll ist, die Zeichnung mit einem satten rot beginnt, während im Laufe der Iteration die weiteren Farben immer blasser werden. Ich fand dies das ästhetisch anspruchvollste Ergebnis, aber um das selber nachvollziehen zu können, solltet Ihr ruhig damit experimentieren, zum Beispiel mit `stroke(theta, 100, 100)` oder `stroke(100-theta, theta, 100)` oder was immer Ihr wollt.

Ihr bekommt so diesen wunderschönen Schmetterling auf den Monitor gezeichnet:

![Screenshot](images/butterflycurve.jpg)

Um die Entstehung der Kurve zu verstehen, empfiehlt *Stan Wagon*[^wagon93], nacheinander folgende Formlen plotten zu lassen:

[^wagon93]: Stan Wagon: *Mathematica® in Aktion*, Heidelberg (Spektrum Akademischer Verlag) 1993

In Polarkoordinaten:

~~~python
r = exp(cos(theta))  # ergibt eine Art Kreis
r = -2*cos(4*theta)  # ergibt eine Art Blume
r = exp(cos(theta)) - 2*cos(4*theta)  # ergibt einen sehr einfachen Schmetterling
~~~

Dann in kartesischen Koordinaten:

~~~python
x = -2*cos(4*theta)
y = -sin(theta/12)**5
~~~

Und dann ruhig auch noch einmal (wieder in Polarkoordinaten):

~~~python
r = exp(cos(theta)) - 2*cos(4*theta) - (sin(theta/12))**5
~~~

Ihr seht dann, daß es eigentlich unerheblich ist, ob Ihr den Störungsgteil der Formel addiert oder subtrahiert: Der Schmetterling ist nahezu identisch, lediglich an der anderen Farbgebung erkennt Ihr, daß es zwei verschiedene Formeln sind.

Die Schmetterlingskurve und ähnliche Kurven wurden von *Temple Fay*[^fay89] an der Universität von Southern Mississpi entwickelt. Sie eignen sich vorzüglich zum Experimentieren. So weist Pickover[^pick92] darauf hin, daß die Kurve

[^fay89]: Temple Fay: *The Butterfly Curve*, American Math. Monthly, 96(5); 442-443
[^pick92]: Clifford A. Pickover: *Mit den Augen des Computers. Phantastische Welten aus dem Geist der Maschine*, München (Markt&Technik) 1992, S. 41ff.

~~~python
r = exp(cos(theta)) - 2.1*cos(6*theta) + sin(theta/30)**7
~~~

eine bedeutend größere Wiederholungsperiode besitzt. Ihr solltet Euch auch das ruhig einmal ansehen. Interessante Vergleiche mit der Originalschmetterlingskurve können Ihr auch ziehen, wenn Ihr mit

~~~python
r = exp(cos(2*theta)) - 1.5*cos(4*theta)
~~~

eine ganz simple Form des Schmetterlings zeichnen lasst. Denn die heutigen Rechner sind schließlich hinreichend schnell, daß Ihr nicht mehr minuten- oder gar stundenlang auf ein Ergebnis warten müßt und zum anderen lädt die Möglichkeit des schnellen Skizzierens mit der Processing-IDE geradezu zu eigenen Experimenten ein.


## Der Lorenz-Attraktor, eine Ikone der Chaos-Theorie

Nachdem ich im letzten Abschnitt die Schmetterlingskurve mit Processing.py gezeichnet hatte, wollte ich nun darauf aufbauen und eine Ikone der Chaos-Forschung, den [Lorenz-Attraktor](https://de.wikipedia.org/wiki/Lorenz-Attraktor) damit zeichnen. Ich hatte das ja auch schon einmal [mit R getan](http://blog.schockwellenreiter.de/essays/lorenzr.html) -- dort findet Ihr auch weitere Hintergrundinformationen zu diesem Attraktor --, aber mit R wurde nur das fertige Ergebnis visualisiert. Hier kommt es mir aber wieder darauf an, die Entstehung der Kurve verfolgen zu können und dafür ist, wie schon bei der Schmetterlingskurve, Processing gut geeignet:

![Screenshot](images/lorenzprocessingpy.jpg)

Als einer der ersten hatte  1961 [Edward N. Lorenz](http://de.wikipedia.org/wiki/Edward%20N.%20Lorenz), ein Meteorologe am [Massachusetts Institute of Technology](http://de.wikipedia.org/wiki/Massachusetts%20Institute%20of%20Technology) (MIT), erkannt, daß Iteration Chaos erzeugt. Er benutzte dort einen Computer, um ein einfaches nichtlineares Gleichungssystem zu lösen, das ein simples Modell der Luftströmungen in der Erdatmosphäre simulieren sollte. Dazu benutzte er ein System von sieben Differentialgleichungen, das [Barry Saltzman](http://www.yale.edu/opa/arc-ybc/v29.n18/story18.html) im gleichen Jahr aus den [Navier-Stokes-Gleichungen](http://de.wikipedia.org/wiki/Navier-Stokes-Gleichungen) [^5_4] hergeleitet hatte. Für dieses System existierte keine analytische Lösung, also mußte es numerisch (d.h. wie damals und auch heute noch vielfach üblich in FORTRAN) gelöst werden. Lorenz hatte entdeckt, daß bei nichtperiodischen Lösungen der Gleichungen vier der sieben Variablen gegen Null strebten. Daher konnte er das System auf drei Gleichungen reduzieren:

[^5_4]: Eine sehr schöne Einführung in [das ungelöste Problem der Navier-Stokes-Gleichungen](http://scienceblogs.de/astrodicticum-simplex/2017/01/20/sternengeschichten-folge-217-das-ungeloeste-problem-der-navier-stokes-gleichungen/) gibt es von *Florian Freistetter* in der 217. Folge seiner *Sternengeschichten*


\begin{align}
\frac{dx}{dt} & = -\sigma (y - z) \\
\frac{dy}{dt} & = (\rho - z)x - y \\
\frac{dz}{dt} & = xy - \gamma z
\end{align}


Dabei sind $\sigma = -10$, $\rho = 40$ und $\gamma = - \frac{8}{3}$. Die Parameter der Gleichung habe ich *[Herm1994]* entnommen, *[Stew1993]* gibt $\rho = 28$ an, aber der Wert ändert nichts an dem Verhalten der Kurve und $\rho = 40$ füllt das Fenster einfach besser aus. 😜

Processing.py besitzt im Gegensatz zu R oder [NumPy](http://cognitiones.kantel-chaos-team.de/programmierung/python/numpy.html) kein Modul zur numerischen Lösung von Differentialgleichungen und so habe ich das einfache [Eulersche Poligonzugverfahren](https://de.wikipedia.org/wiki/Explizites_Euler-Verfahren) zur numerischen Berechnung benutzt

~~~python
    dx = -sigma*(x - y)*dt
    dy = (x*(r - z) - y)*dt
    dz = (x*y - b*z)*dt
    x += dx
    y += dy
    z += dz
~~~

und dabei konstant `dt = 0.01` gesetzt. Das benötigt natürlich mehr Rechenkapazität, als sie Lorenz je zur Verfügung standen, aber trotz der größeren Genauigkeit ändert sich nichts am chaotischen Verhalten der Kurve. Für die Farbberechnugn habe ich dieses mal nur den Farbwert (*Hue*) bei jeder Iteration geändert, Sättigung (*Saturation*) und Helligkeit (*Brightness*) bleiben konstant auf dem höchsten Wert. Das ergibt kräftige Farben, die von Rot über Orange nach Gelb und dann nach Grün, Blau und Violett wandern. So kann man schön erkennen, daß die beiden »Flügel« des Attraktors immer wieder, aber für uns unvorhersehbar, durchlaufen werden.

### Der Quellcode

Hier nun der vollständige Quellcode des Skripts. Er ist kurz und selbsterklärend und folgt weitestgehend dem Pascal-Programm aus *[Herm1994]*, Seiten 80ff.

~~~python
b = 8.0/3
r = 40.0
sigma = 10.0
dt = 0.01
x = y = 0.01
z = t = 0.0
xOld = zOld = 0.0
first = True

def setup():
    size(640, 480)
    background(0)
    colorMode(HSB, 100)

def draw():
    global x, y, z, t, xOld, zOld
    global first
    strokeWeight(1)
    stroke(t, 100, 100)
    dx = -sigma*(x - y)*dt
    dy = (x*(r - z) - y)*dt
    dz = (x*y - b*z)*dt
    x += dx
    y += dy
    z += dz
    # auf Fenstergröße skalieren
    xx = (x*8) + 320
    zz = 470 - (z*5.5)
    if first:
        point(xx, zz)
    else:
       line(xOld, zOld, xx, zz)
    xOld = xx
    zOld = zz
    first = False 
    t = t + dt
    if ( t >= 75.0):
       print("I did it, Babe!")
       noLoop()
~~~

### Links

  * Der *[Lorenz Attractor](http://mathworld.wolfram.com/LorenzAttractor.html)* auf Wolfram MathWorld

### Literatur

  * *[Herm1994]* Dieter Hermann: *Algorithmen für Chaos und Fraktale*, Bonn (Addison-Wesley) 1994, S. 80ff.
  * *[Pief1991]* Frank Piefke: *Simulationen mit dem Personalcomputer*, Heidelberg (Hüthig) 1991
  * *[Stew1993]* Ian Stewart: *Spielt Gott Roulette?*, Frankfurt (Insel TB) 1993

# Shapes

## For Your Eyes Only – Processing.py zieht Kreise

Nachdem ich in den vorherigen Tutorials zu Processing.py, dem Python-Mode von Processing, schon mit Punkten und Linien hantiert habe, wird es nun Zeit, etwas mit Kreisen und Ellipsen anzustellen (sie werden in Processing mit dem gleichen Befehl erzeugt).

![Wo bleibt das Lächeln?](images/foryoureyesonly.jpg)

Ein einfacher Kreis ist schnell erzeugt. Mit diesem kleinen *Sketch* malt Ihr einen grellroten Kreis auf schwarzem Grund:

~~~python
def setup():
    size(500, 500)

def draw():
    background(0)
    fill(255, 0, 0)
    ellipse(width/2, height/2, 450, 450)
~~~

Die Funktion `ellipse()` besitzt vier Parameter, die ersten beiden sind die x- und y-Koordinaten, die per Default die Mitte des Kreises oder der Ellipse bezeichnen, die beiden anderen sind der Durchmesser des Kreises oder der Ellipse (auch wenn sie in der Literatur oft mit `r` bezeichnet werden, nicht der Radius). Bei einem Kreis müssen die letzten beiden Parameter immer den gleichen Wert besitzen. Wenn Ihr aber zum Beispiel die Funktion mit

~~~python
    ellipse(width/2, height/2, 350, 450)
~~~

oder

~~~python
    ellipse(width/2, height/2, 450, 350)
~~~

aufruft, dann seht Ihr, wie aus den Kreisen Ellipsen werden.

Nun steht Processing aber für Interaktivität. Daher möchte ich aus fünf Kreisen ein Gesicht zaubern, dessen Pupillen dem Mauszeiger folgen. Auch dieser *Sketch* ist hübsch kurz geraten:

~~~python
def setup():
    size(300, 300)
    strokeWeight(3)

def draw():
    background(139, 134, 130)
    face()
    eye(110, height/2)
    eye(190, height/2)

def face():
    fill(244, 244, 0)
    ellipse(width/2, height/2, 160, 160)

def eye(x, y):
    fill(255)
    ellipse(x, y, 60, 60)
    # Die Pupillen folgen der Maus
    mx = mouseX - x
    my = mouseY - y
    fill(50)
    ellipse(x + mx/12, y + my/12, 25, 25)
~~~

Es wäre nicht wirklich notwendig gewesen, aber der Modularität willen habe ich das Zeichnen des Gesichtes in die Funktion `face()` und das Zeichnen der Augen in die Funtion `eye()` ausgelagert. Mit den Werten in dem `ellipse()`-Aufruf bei den Augen habe ich solange experimentiert, bis sie meinen Vorstellungen entsprachen. Nun sieht aber alles aus wie in dem obigen Screenshot.

### Credits

Die Idee zu den Augen habe ich einem [(Java-) Processing-Tutorial](https://lernprocessing.wordpress.com/2010/01/10/funktionen/) von *Thomas Koberger* entnommen, das ich variiert und nach Processing.py übertragen habe. Auf [seinen Seiten](https://lernprocessing.wordpress.com/2010/01/18/processing-links/) findet man übrigens noch viele weitere, interessante und lehrreiche Tutorials, so daß ich Euch einen Besuch dort empfehle.

Für die Farben habe ich mal wieder wild nach einer [Seite mit Farbpaletten](http://www.farb-tabelle.de/de/farbtabelle.htm) gegoogelt und fand die gefundene dann zwar nicht unbedingt schön, aber ungemein praktisch.

## Spaß mit Kreisen: Konfetti

Der folgende kleine Sketch ist nicht mehr als eine Fingerübung. Er soll Euch zeigen, wie man schon mit wenigen Zeilen Code und Processings-Zufallsfunktion `random()` viele bunte Konfetti-Schnipsel auf den Bildschirm zaubern kann:

![Konfetti](images/konfetti.jpg)

Und hier der Quellcode des Sketches in Processing.py:

~~~python
def setup():
    size(400, 400)
    frame.setTitle("Konfetti!")
    background(0)

def draw():
    x = random(width)
    y = random(height)
    dia = random(5, 25)
    r = random(255)
    g = random(255)
    b = random(255)
    fill(r, g, b)
    ellipse(x, y, dia, dia)
~~~

Für so wenige Programmzeilen ist das Ergebnis doch recht ansprechend, oder?

## Syntaktischer Zucker: »with« in Processing.py

Wenn man in Processing.py irgendetwas zum Beispiel zwischen `beginShape()` und `endShape()` klammert, fühlt sich das nicht sehr »pythonisch« an. Ich denke dann die ganze Zeit: Das gehört doch eingerückt! In Processings Java-Mode kann man das auch machen, weil man in Java Leerzeichen einsetzen kann, wie man will -- sie haben dort keine Bedeutung. Doch Python reagiert ja sehr sensibel auf Einrückungen, da hier Leerzeichen Teil der Syntax sind. Aber die Macher von Processing.py haben dies bedacht und uns einen Ausweg aus diesem Dilemma geboten: Das `with`-Statement.

![Screenshot](images/withprocessingpy.jpg)

In seiner einfachsten Form sieht das so aus. Statt zum Beispiel

~~~python
def setup():
    size(400, 400)
    background(255)

def draw():
    fill(color(255,  153,  0))
    strokeWeight(1)
    ellipse(100, 100, 50, 50)
    fill(color(255,  51,  51))
    strokeWeight(5)
    ellipse(200, 200, 50, 50)
    fill(color(255,  153,  0))
    strokeWeight(1)
    ellipse(300, 300, 50, 50)
~~~

zu schreiben, schreibt man einfach:

~~~python
def setup():
    size(400, 400)
    background(255)
    

def draw():
    fill(color(255,  153,  0))
    ellipse(100, 100, 50, 50)
    
    with pushStyle():
        fill(color(255,  51,  51))
        strokeWeight(5)
        ellipse(200, 200, 50, 50)
    ellipse(300, 300, 50, 50)
~~~

Die Ausgabe ist in beiden Fällen identisch, aber der zweite Sketch ist in meinen Augen bedeutend eleganter und fühlt sich viel pythonischer an. Außerdem erspart man sich viel Tipparbeit. 😜

Da ich die Verwendung des `with`-Statements auch erst durch eines der mitgelieferten Beispielprogramme herausbekommen habe, hier eine (hoffentlich) komplette Liste der Möglichkeiten:

~~~python
    with pushMatrix():          pushMatrix()
        translate(10, 10)       translate(10, 10)
        rotate(PI/3)            rotate(PI/3)
        rect(0, 0, 10, 10)      rect(0, 0, 10, 10)
    rect(0, 0, 10, 10)          popMatrix()
                                rect(0, 0, 10, 10)

with beginContour():             beginContour()
    doSomething()                doSomething()
                                 endContour()


with beginCamera():              beginCamera()
    doSomething()                doSomething()
                                 endCamera()

with beginPGL():                 beginPGL()
    doSomething()                doSomething()
                                 endPGL()

with beginShape():               beginShape()
    vertex(x, y)                 vertex(x, y)
    vertex(j, k)                 vertex(j,k)
                                 endShape()
    
    
with beginShape(TRIANGLES):      beginShape(TRIANGLES)
    vertex(x, y)                 vertex(x, y)
    vertex(j, k)                 vertex(x, y)
                                 endShape()

with beginClosedShape():         beginShape()
    vertex(x, y)                 vertex(x, y)
    vertex(j, k)                 vertex(j, k)
                                 endShape(CLOSED)
~~~

Links steht die Schreibweise mit dem `with()-Statement`, rechts die traditionelle Form. Abgesehen davon, daß die `with`-Schreibweise immer mindestens eine Zeile kürzer ist, sorgt sie durch die Einrückungen auch für eine bessere Übersicht und eine bessere Lesbarkeit.



## Spaß mit Kreisen (2) in Processing.py: Cantor-Käse und mehr

![Kein Cantor-Käse](images/keincantorkaese-s.jpg)

Wie im letzten Beitrag gezeigt, ist es in Processing (und damit auch in Processing.py, dem Python-Mode für Processing) recht einfach, einfache Kreise oder Ellipsen zu zeichnen. Aber das ist auf die Dauer natürlich ein wenig langweilig, daher wende ich mich nun einer rekursiven Figur zu, die zwar ebenfalls nur aus Kreisen besteht, aber dennoch einige interessante Eigenschaften aufweist, dem **Cantor-Käse**, einer Figur, die der [Cantor-Menge](https://de.wikipedia.org/wiki/Cantor-Menge) topologisch ähnlich ist. Sie wird konstruiert, in dem aus einem Kreis bis auf zwei kleinere Kreise alles entfernt wird. Aus diesen zwei kleineren Kreisen wird wiederum bis auf zwei kleinere Kreise alles entfernt. Nun hat man schon vier Kreise, aus denen man jeweils bis auf zwei kleinere Kreise alles entfernt. Und so weiter und so fort …

![Cantor-Käse](images/cantorcheeseprocpy.jpg)

Das schreit natürlich nach einer rekursiven Funktion und die ist in Python (genauer: in Processings Python-Mode) recht schnell erstellt:

~~~python
def setup():
    size(500, 500)
    # colorMode(HSB, 100, 100, 100)
    noLoop()

def draw():
    cheese(width/2, height/2, 500, 10)

def cheese(x, y, r, level):
    ellipse(x, y, r, r)
    if (level > 1):
        cheese(x - r/4, y, r/2, level-1)
        cheese(x + r/4, y, r/2, level-1)
~~~

Das Ergebnis könnt Ihr in obenstehenden Screenshot bewundern. Im Screenshot sieht man noch, daß ich auch versucht habe, mit Farbe zu experimentieren, aber ein wirklich befriedigendes Ergebnis war dabei nicht herausgekommen

Ich hatte diese Figur auch schon mal in [Shoes zeichnen lassen](http://blog.schockwellenreiter.de/2016/05/2016050302.html) und dabei Porbleme mit der Rekursiontiefe festgestellt (ab einer Rekursionstiefe von 15 stürzte Shoes gnadenlos ab). Hier scheint Processing robuster zu sein, eine Rekursionstiefe von 15 nahm die Software gelassen hin, ließ sich dann natürlich Zeit mit der Ausgabe. Das muß schließlich alles berechnet werden.

Weil der Durchmesser der Kreise in der Literatur oft mit `r` bezeichnet wird, neige ich dazu, Radius und Durchmesser zu verwechseln. Setzt man dann den Algorithmus 1:1 um, zum Beispiel wie in diesem Sketch

~~~python
def setup():
    size(1000, 500)
    noLoop()

def draw():
    cheese(width/2, height/2, 500, 10)

def cheese(x, y, r, level):
    ellipse(x, y, r, r)
    if (level > 1):
        cheese(x - r/2, y, r/2, level-1)
        cheese(x + r/2, y, r/2, level-1)
~~~

kommt die Figur heraus, die den Kopf dieses Beitrages ziert. Das ist zwar streng genommen kein Cantor-Käse mehr, aber dennoch ein interessantes Ergebnis. Das macht den Vorteil des schnellen Skizzierens in Processing aus: Selbst Fehler können unerwartete und notierenswerte Ergebnisse liefern. Man hebt dann den Sketch einfach auf.

### Cantors Doppelkäse

Schon bei meinen Experimenten mit Shoes [hatte ich mich gefragt](http://blog.schockwellenreiter.de/2016/09/2016091601.html), wie es denn aussähe, wenn man diese Figur sich nicht nur in der Horizontalen, sondern auch in der Vertikalen ausbreiten läßt?

![Doppelkäse](images/doppelkaeseprocpy.jpg)

Dabei habe ich auch gleich ein interaktives Element eingeführt: Startet man das Programm, zeigt es zuerst nur ein weißes Fenster, nach dem ersten Mausklick sieht man die erste Rekursionstiefe, einen einfachen Kreis, der nächste Mausklick zeigt vier darin eingeschriebene Kreise, der nächste Mausklick zeigt dann in jedem der kleinen Kreise wiederum vier eingeschriebene Kreise und so weiter und so fort …

~~~python
maxlevel = 7

def setup():
    global i
    i = 1
    size(500, 500)
    # colorMode(HSB, 100, 100, 100)
    background(255)
    noFill()

def draw():
    pass

def cheese(x, y, r, level):
    ellipse(x, y, r, r)
    if (level > 1):
        cheese(x - r/4, y, r/2, level-1)
        cheese(x, y - r/4, r/2, level-1)
        cheese(x + r/4, y, r/2, level-1)
        cheese(x, y + r/4, r/2, level-1)

def mousePressed():
    global i
    cheese(width/2, height/2, 500, i)
    i += 1
    if (i >= maxlevel):
        noLoop()
~~~

Das Programm stoppt dann bei einer Rekursionstiefe von sieben. Auch hier ist Processing robuster als Shoes, höhere Rekursionstiefen waren kein Problem, nur man sah dann nicht viel mehr als ein auf der Spitze stehendes Quadrat mit ein paar Ausbuchtungen -- die Auflösung des Bildschirms setzt hier neuem Erkenntnisgewinn Grenzen.

Interessant und neu für mich war, daß man -- um überhaupt ein Zeichenfenster zu bekommen, in das man mit der Maus klicken konnte -- eine leere `draw()`-Funktion benötigte. Eigentlich logisch, aber ich hatte vorher nie darüber nachgedacht.

### Literatur

- Clifford A. Pickover: *Mit den Augen des Computers. Phantastische Welten aus dem Geist der Maschine*, München (Markt und Technik) 1992. Diese deutsche Übersetzung von *Computers and the Imagination* ist eine geniale Fundgrube für alle, die Simulationen und mathematische Spielereien mit dem Computer lieben. Es ist eines der besten Bücher [Pickovers](http://cognitiones.kantel-chaos-team.de/personen/pickover.html). Dem Cantor-Käse ist auf den Seiten 171-181 ein eigenes Kapitel gewidmet.
- Chris Robart: *[Programming Ideas: For Teaching High School Computer Programming](http://mmhs.ca/compsci/ideas2.pdf)*, (PDF 260 KB, 2nd Edition) 2001. Ebenfalls eine Fundgrube voller Ideen, deren Download sich in jedem Fall lohnt.

## Weitere geometrische Grundformen

Processing besitzt ein kleines Set von geometrischen Primitiven in 2D (im Englischen *Shapes* genannt) mit denen sich so einiges anstellen läßt. Neben den schon bekannten Punkten und Kreisen und Ellipsen, gibt es noch einige andere, die ich der Reihe nach vorstellen möchte:

![Screenshot](images/shapes.jpg)

### Rechtecke

Rechtecke (`rect()`) sind die einfachste Grundform. Dennoch besitzen auch sie einige Besonderheiten. Es gibt sie nämlich in der Form

~~~python
rect(x, y, w, h)
rect(x, y, w, h, r)
rect(x, y, w, h, tl, tr, br, bl)
~~~

Bei vier Parametern sind die ersten beiden Parameter, die x- und y-Koordinate der linken, oberen Ecke des Rechtecks und die beiden anderen Parameter geben die Breite und Höhe des Rechtecks an. Gilt `w == h`, dann ist das Rechteck natürlich ein Quadrat.

Wird `rect()` mit fünf Parametern aufgerufen, dann ist der fünfte Parameter als Radius für die Abrundung der Ecken verantwortlich. Mit acht Paramtern bekommt jede Ecke einen eigenen Radius für die abgerundeten Ecken einen eigenen Radius zugeschrieben. Dabei wird von *links oben* über *rechts oben* und *rechts unten* nach *links unten* vorgegangen.

Rechtecke besitzen per Default den `rectMode(CORNER)`. Wird ein anderer `rectMode()` eingegeben, dann ändert sich die Bedeutung des dritten und vierten Parameters. Ist er `CORNERS`, dann bennen die ersten beiden Paramter weiterhin die linke, obere Ecke, der dritte und vierte Parameter aber die x- und y-Koordinaten der rechten, unteren Ecke.

Ist der `rectMode(CENTER)`, dann bennen die ersten beiden Parameter den Mittelpunkt des Rechteckes, der dritte und vierte Parameter gibt aber weiterhin die Breite und Höhe des Rechtecks an.

Dahingegen sind beim `rectMode(RADIUS)` die ersten beiden Paramter die x- und y-Koordinaten des Mittelpunkts des Rechtecks, während die dritte und vierte Koordinate jeweils die Hälfte der Breite und die Hälfte der Höhe angeben.

Der `rectMode(CENTER)` ist vor allen Dingen dann vom Vorteil, wenn Rechtecke mit Kreisen oder Ellipsen koordiniert werden, da bei diesen per Default `ellipseMode(CENTER)` gilt. Zu diesen kommen ich daher im Anschluß [noch einmal](http://py.kantel-chaos-team.de/foryoureyesonly/).

### Kreise und Ellipsen

Ellipsen und Kreise (als Spezialform der Ellipse) werden in Processing mit dem Befehl

~~~python
ellipse(x, y, w, h)
~~~

erzeugt. Dabei sind `x` und `y` der Mittelpunkt der Ellipse und `w` und `h` per Default die Breite und Höhe der Ellipse. Sind `w == h`, dann bildet die Ellipse einen Kreis.

Ändert man jedoch den Default-Mode `CENTER`, dann ergeben sich folgende Bedeutungsänderungen der vier Parameter.

Beim `ellipseMode(RADIUS)` bilden die ersten beiden Parameter weiterhin den Mittelpunkt der Ellipse oder des Kreises, der dritte und vierte Parameter gibt jedoch die Hälfte der Höhe und die Hälfte der Breite der Ellipse oder des Kreises an.

Ist der `ellipseMode(CORNER)`, dann benennen die x- und y-Koordinaten die linke, obere Ecke der Ellipse oder des Kreises, die beiden anderen Parameter geben weiterhin die Breite und Höhe an.

Heißt es jedoch `ellipseMode(CORNERS)`, dann bennenen die x- und y-Koordinaten die linke, obere Ecke des die Ellipse oder den Kreis umschließenden Rechtecks, der dritte und vierte Parameter die rechte untere Ecke dieses Rechtecks.

!!! tip "Achtung"
    Die Modes `CORNER`, `CORNERS`, `CENTER` und `RADIUS` müssen immer in Großbuchstaben eingegeben werden, da Processing und Python streng zwischen Groß- und Kleinschreibung unterscheiden.

### Dreieck

Das Dreieick ist eines der einfachsten geometrischen Grundformen in Processing. Es existiert nur in der Form

~~~python
triangle(x1, y1, x2, y2, x3, y3)
~~~

und hat auch keinen besonderen Mode. Die jeweiligen x- und y-Koordinagen sind die Koordinaten des ersten, zweiten und dritten Punktes. Bei der Reihenfolge wird -- oben beginnend -- immer im Uhrzeigersinn vorgegangen. Das ist alles.

### Unregelmäßige Vierecke

Ähnlich einfach verhält es sich mit den unregelmäßigen Vierecken. Sie werden mit

~~~python
quad(x1, y1, x2, y2, x3, y3, x4, y4)
~~~

erzeugt und auch hier sind es absolute Koordinaten und das Gebilde besitzt ebenfalls keinen besonderen Mode. Auch hier wird bei der Zählung links oben begonnen und dann werden die Ecken ebenfalls im Uhrzeigersinn abgearbeitet.

### Kreisbögen

Kreisbögen sind mit der Ellipse (genauer: dem Kreis verwandt) und besitzen die gleichen Modi wie diese (mit dem gleichen Default `CENTER`). Sie werden wie folgt aufgerufen:

~~~python
arc(x, y, w, h, start, stop)
arc(x, y, w, h, start, stop, mode)
~~~

Die x- und y-Koordinaten sind im Default-Mode der Mittelpunkt des Kreises, während `w` und `h` im Default-Mode die Breite und Höhe des Kreisen angeben. `start` und `stop` sind die Winkel (in *radians*) für die Länge des Kreisbogens.

Dann gibt es hier noch einen besonderen `mode`. Der kann `OPEN` (das ist der Default), `CHORD` oder `PIE` heißen. Im Default `OPEN` bleibt der Kreisbogen offen, falls es jedoch ein `fill()` gibt, wird er dennoch gefüllt. Bei `CHORD` wird der Kreisbogen geschlossen und bei `PIE` bildet er ein Kuchenstück, wie man es von Tortengraphiken kennt.


### Der Quelltext

In diesem Beispielprogramm habe ich alle angesprochenen geometrischen Primitive in ihren diversen Erscheinungsformen zeichnen lassen. Mit dem oben geschriebenen dürfte es einfach nachzuvollziehen ein.

~~~python
def setup():
    size(640, 640)
    frame.setTitle("Geometrische Grundformen in Processing.py")
    # noLoop()

def draw():
    background(255)
    drawGrid()
    stroke(0)
    
    # Rechtecke
    with pushStyle():
        fill(255,127,36)
        rect(20, 20, 120, 120)
        rect(180, 20, 120, 120, 20)
        rect(340, 20, 120, 120, 20, 10, 40, 80)
        rect(500, 60, 120, 80)
    
    # Kreise und Ellipsen
    with pushStyle():
        fill(107, 142, 35)
        ellipse(80, 240, 120, 120)
        ellipse(240, 240, 120, 80)
        ellipse(400, 240, 80, 120)
    
    # Dreiecke
    with pushStyle():
        fill(255, 236, 139)
        triangle(560, 180, 620, 300, 500, 300)
        triangle(20, 340, 140, 460, 20, 460)
        
    # Vierecke
    with pushStyle():
        fill(193, 205, 193)
        quad(180, 340, 300, 340, 300, 400, 180, 460)
        quad(400, 340, 460, 400, 400, 460, 340, 400)
        quad(500, 340, 620, 400, 500, 460, 560, 400)
    
    # Kreisbögen
    with pushStyle():
        fill(204, 53, 100)
        arc(80, 560, 120, 120, 0, HALF_PI)
        with pushStyle():
            noFill()
            arc(80, 560, 130, 130, HALF_PI, PI)
            arc(80, 560, 140, 140, PI, PI+QUARTER_PI)
            arc(80, 560, 150, 150, PI+QUARTER_PI, TWO_PI)
        arc(240, 560, 120, 120, 0, PI+QUARTER_PI, OPEN)
        arc(400, 560, 120, 120, 0, PI+QUARTER_PI, CHORD)
        arc(560, 560, 120, 120, QUARTER_PI, TWO_PI-QUARTER_PI, PIE)
    

def drawGrid():
    stroke(200, 200, 255)
    for i in range(0, width, 20):
        line(i, 0, i, height)
    for i in range(0, height, 20):
        line(0, i, width, i)
~~~

Ich habe das Fenster mit einem 20 x 20 Pixel großen Raster wie auf kariertem Schulpapier versehen, damit Ihr die Eckpunkte der einzelnen Shapes auszählen könnt, falls Euch die Koordinaten nicht sofort klar werden.

### Credits

Teilweise folgt dieser Sketch einer Idee von *Jan Vantomme* aus seinem Buch »Processing 2: Creative Coding Programming Cookbook« (Seiten 31 ff.). Ich habe sie abgewandelt, die Beispiele für die Kreisbögen hinzugefügt und vom Java-Mode in den Python-Mode übertragen.


## Eine analoge Uhr aus Kreisbögen

In seiner 74. Coding-Challenge auf YouTube zeigte *Daniel Shiffman*, wie man mit P5.js, dem JavaScript-Mode von Processing eine analoge Uhr aus Kreisbögen programmiert. Inspiriert wurde er von *John Maedas* [12 o'Clocks](http://cmuems.com/2016/60212/lectures/lecture-09-09b-clocks/maedas-clocks/)-Projekt und ich unterlag der Versuchung, *Shiffmans* JavaScript-Programm nach Processing.py zu portieren:

![Eine analoge Uhr aus Kreisbögen](images/clockpy.jpg)

Dabei habe ich gegenüber dem Original-Script nur einige kleine Veränderungen vorgenommen.Ich habe die Stunden in den äußeren Kreisbogen gelegt und dadurch die Sekunden in den inneren Kreisbogen. Und ich habe die Zeiger der Uhr nicht nur in unterschiedlichen Längen, sondern auch in unterschiedliche Dicken zeichnen lassen, wie man es von analogen Uhren gewohnt ist. Außertdem habe ich heftigen Gebrauch vom `with`-Statement gemacht, das in Processing.py in vielen Fällen nicht nur das `push` und `pop` ersetzen, sondern auch ungterschiedliche Statii klasmmern kann.

### Der Quellcode

Meiner Meinung nach ist der Quellcode gegenüber der JavaScript-Version übersichtlicher geworden und leichter zu durchschauen. Das liegt aber sicher nicht an meinen genialen Programmierkenntnissen (die sind eher bescheiden), sondern ist der Klarheit von Python geschuldet:

~~~python
baseStroke = 8

def setup():
    size(400, 400)
    frameRate(30)
    
def draw():
    background(0)
    translate(width/2, height/2)
    rotate(radians(-90))
    
    hr = hour()
    mn = minute()
    sc = second()
    
    secondAngle = map(sc, 0, 60, 0, 360)
    minuteAngle = map(mn, 0, 60, 0, 360)
    hourAngle = map(hr%12, 0, 12, 0, 360)
    noFill()
    strokeWeight(baseStroke)
    
    # Kreisbögen
    with pushStyle(): # Sekunden
        stroke(150, 100, 255)
        arc(0, 0, 300, 300, radians(0), radians(secondAngle))
    with pushStyle(): # Minuten
        stroke(255, 100, 150)
        arc(0, 0, 320, 320, radians(0), radians(minuteAngle))
    with pushStyle(): # Stunden
        stroke(150, 255, 100)
        arc(0, 0, 340, 340, radians(0), radians(hourAngle))

    # Zeiger
    with pushMatrix(): # Sekunden
        strokeWeight(baseStroke/4)
        stroke(150, 100, 255)
        rotate(radians(secondAngle))
        line(0, 0, 100, 0)
    with pushMatrix(): # Minuten
        strokeWeight(baseStroke/2)
        stroke(255, 100, 150)
        rotate(radians(minuteAngle))
        line(0, 0, 80, 0)
    with pushMatrix(): # Stunden
        strokeWeight(baseStroke)
        stroke(150, 255, 100)
        rotate(radians(hourAngle))
        line(0, 0, 60, 0)

    noStroke()
    fill(255, 255, 255)
    ellipse(0, 0, 10, 10)
~~~

### Links

- *Golan Levins* [Notizen](http://cmuems.com/2016/60212/lectures/lecture-09-09b-clocks/maedas-clocks/) zu Maedas 12 o’Clocks nebst [Anhang](http://cmuems.com/2016/60212/lectures/lecture-09-09b-clocks/)
- [Alca's Clock Collection](https://codepen.io/collection/DqRNLQ/) auf CodePen

## Visualisierung: Die Sonntagsfrage

![Screenshot](images/sonntagsfrage.jpg)

Man kann sich durchaus zu Recht fragen, ob es überhaupt sinnvoll ist, so etwas wie den obigen Barchart in Processing.py per Fuß zu erstellen. Schließlich gibt es (auch in Python) Bibliotheken wie etwa die [Matplotlib](http://cognitiones.kantel-chaos-team.de/programmierung/python/matplotlib.html), die für diese Aufgabe spezialisiert sind und mit wenigen Zeilen Code wunderbarer Graphiken auf den Monitor zaubern und sie auch gleichzeitig publikationsreif in einer Datei ablegen können.

Aber auf der anderen Seite schadet es nichts, wenn man selber genau weiß, wie man so etwas anstellen kann. Denn zum einem hat man vielleicht Gründe, die Umgebung von Processing.py nicht verlassen zu wollen. Und zum anderen gibt es doch auch immer wieder Spezialfälle, die von den spezialisierten Bibliotheken nicht abgedeckt werden.

Daher habe ich hier einmal die Ergebnisse der Sonntagsfrage (»Wenn am nächsten Sonntag Bundestagswahl wäre …«), die die *Forschungsgruppe Wahlen* regelmäßig veröffentlicht, nur mit den Hausmitteln von Processing.py in einem einfachen Barchart dargestellt.

Für die Daten, Namen und Farben habe ich drei Listen erstellt. Das hat den Vorteil, daß man bei einer neuen Umfrage nur die Ergebnisse in der Liste `prozente[]` ändern muß -- an den anderen Listen ändert sich zumindest bis zur Bundestagswahl im nächsten Jahr nichts.

Normalerweise werden Rechtecke in Processing ja mit dem Befehl `rect(x, y, w, h)` erzeugt, setzt man jedoch `rectMode(CORNERS)`, dann werden die realen Eckpunkte als Parameter erwartet, also `rect(x1, y1, x2, y2)`.

Für die Anpassung der Balken an den Bildschirmausschnitt habe ich auf Processings `map(value, dataMin, dataMax, targetMin, targetMax)`-Funktion zurückgegriffen, die einen Datenwert von einem Bereich in einen anderen überträgt. Nun hat Python selber aber auch noch eine eingebaute `map(function, iterable, …)`-Funktion, die mit der Processing-Funktion in Konflikt steht. Aber die Macher von Processing.py haben sich viel Mühe gegeben, diesen Konflikt aufzulösen. Erfüllt `map()` die Signatur der Python-Funktion, wird diese aufgerufen, ansonsten die Processing-Funktion.

### Der Quellcode

~~~python
parteien = ["CDU/CSU", "SPD", u"Grüne", "FDP", "Linke", "AfD", "Sonstige"]
prozente = [34, 32, 7, 5, 8, 9, 5]
farben = [color(0, 0, 0), color(255, 48, 48), color(240, 230, 140),
          color(238, 238, 0), color(238, 18, 37),
          color(65, 105, 225), color(190, 190, 190)]

titel = "Die Sonntagsfrage"

def setup():
    global X1, X2, Y1, Y2
    size(720, 405)
    X1 = 50
    X2 = width - X1
    Y1 = 60
    Y2 = height - Y1
    font1 = createFont("OpenSans-Regular.ttf", 20)
    textFont(font1)
    noLoop()

def draw():
    global X1, X2, Y1, Y2
    fill(255)
    rectMode(CORNERS)
    rect(X1, Y1, X2, Y2)
    fill(0)
    textSize(20)
    text(titel, X1, Y1 - 10)
    delta = (X2 - X1)/(len(prozente))
    w = delta*0.9
    x = w*1.22
    textSize(12)
    for i in range(len(prozente)):
        # Balken zeichnen
        h = map(prozente[i], 0, 40, Y2, Y1)
        fill(farben[i])
        rect(x - w/2, h, x + w/2, Y2)
        # Parteinamen und Prozente unter der X-Achse
        textAlign(CENTER, TOP)
        fill(0)
        text(parteien[i], x, Y2 + 10)
        text(str(prozente[i]) + " %", x, Y2 + 25)
        x += delta
~~~

Ansonsten ist der Quellcode leicht nachzuvollziehen. Die Abstands- und Längenwerte für `w` und `delta` habe ich durch Experimentieren herausgefunden, ebenso die Startposition von `x`.

### Quellen

Die Zahlen der *Forschungsgruppe Wahlen* habe ich auf der Seite [wahlrecht.de](http://www.wahlrecht.de/umfragen/index.htm) entnommen, dort sind viele weitere Umfrageergebnisse zu Bundes- und Landtagswahlen zu finden. Und den verwendeten Font [Open Sans](https://fonts.google.com/specimen/Open+Sans) habe ich bei Google Fonts gefunden. Er steht unter der [Apache-Lizenz, Version 2](http://www.apache.org/licenses/LICENSE-2.0). Ihr solltet nicht vergessen, die entsprechende Datei `OpenSans-Regular.ttf` in den `data`-Folder Eures Sketches zu schieben, damit Processing.py den Font auch finden kann.

## Rosetten-Kurven

Die [Rosetten-Kurven](https://de.wikipedia.org/wiki/Rosette_(Kurve)), die *Daniel Shiffman* so munter in seiner [55. Code-Challenge](http://blog.schockwellenreiter.de/2017/02/2017021003.html) in [P5.js](http://cognitiones.kantel-chaos-team.de/programmierung/creativecoding/processing/p5js.html), dem JavaScript-Mode von Processing, programmiert hatte, haben mir keine Ruhe gelassen. Ich wollte so etwas auch unbedingt in Processing.py implementieren.

![Rosetten-Kurve](images/rosetten.jpg)

Der Anfang war einfach. Ich bin stur *Daniel Shiffman* gefolgt und hatte innerhalb kürzester Zeit seinen Code in einen Python-Code verwandelt:

~~~python
d = 8.0
n = 5.0

def setup():
    size(400, 400)
    frame.setTitle("Rosetten")
    noFill()

def draw():
    k = n/d
    background(51)
    translate(width/2, height/2)
    with beginClosedShape():
        stroke(255)
        strokeWeight(1)
        a = 0
        while (a < d*TWO_PI):
            r = 200*cos(k*a)
            x = r*cos(a)
            y = r*sin(a)
            vertex(x, y)
            a += 0.02
~~~

Die einzigen Änderungen sind einmal, daß ich das `with`-[Statement](with.md) ausgenutzt und daß ich statt der `for`-Schleife eine `while`-Schleife verwendet habe, da in Pythons `for`-Schleifen das Inkrement oder Dekrement ganzzahlig sein müssen.

Doch bin ich zwar durchaus ein Freund des Sketchens, aber jedesmal, wenn ich eine andere Rosette haben will, den Quelltext zu ändern, war dann doch nicht mein Ding. Daher habe ich dann die `d`- und `n`- Werte, wie sie in dem oben und im Literaturverzeichnis verlinkten Wikipedia-Artikel genannt sind, in eine Liste gepackt

~~~python
dList = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
nList = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
~~~

und aus dieser Liste dann bei jedem Mausklick zufällig je einen Wert für `d` und `n` auswählen lassen:

~~~python
def mousePressed():
    global n, d
    n = r.choice(nList)
    d = r.choice(dList)
~~~

Pythons [Random-Bibliothek](https://docs.python.org/2/library/random.html) stellt dafür dankenswerterweise den Befehl `choice()` zur Verfügung, der diese Listenmanipulation sehr einfach macht.

Der Rest war dann nur noch Kosmetik: In nostalgischer Erinnerung an meine frühen Computerjahre habe ich die Kurve in Grün zeichnen und damit ich weiß, welche Werte der Zufallszahlengenerator mir für `d` und `n` ausgewählt hat, habe ich diese unten rechts ausgeben lassen.

### Der Quelltext

Für die, die diesen Sketch nachprogrammieren wollen, hier nun auch der vollständige Quelltext meines Experiments:

~~~python
import random as r

font = None
dList = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
nList = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
d = 5.0 # Startwert
n = 8.0 # Startwert

def setup():
    size(400, 400)
    frame.setTitle("Rosetten")
    font = createFont("American Typewriter", 12)
    textFont(font)
    noFill()

def draw():
    global n, d
    k = n/d
    background(51)
    translate(width/2, height/2)
    with beginClosedShape():
        stroke(0, 188, 0)
        strokeWeight(1)
        a = 0
        while (a < d*TWO_PI):
            r = 200*cos(k*a)
            x = r*cos(a)
            y = r*sin(a)
            vertex(x, y)
            a += 0.02
        text("n = " + str(n) + ", d = " + str(d), 100, 190)

def mousePressed():
    global n, d
    n = r.choice(nList)
    d = r.choice(dList)
~~~

### Caveat

Als Font für die Textausgabe habe ich mir den Systemfont *»American Typewriter«* ausgesucht (ich mag ihn einfach). Dieser steht sicher nicht auf allen Betriebssystemen zur Verfügung, Ihr müßt Euch daher gegebenenfalls einen anderen Systemfont aussuchen.

### Literatur

- [Rosettenkurven](https://de.wikipedia.org/wiki/Rosette_(Kurve)) in der deutschsprachigen Wikipedia

## Der Baum des Pythagoras

Eine weitere Ikone der fraktalen Geometrie ist der [Pythagoras-Baum](https://de.wikipedia.org/wiki/Pythagoras-Baum). Er geht zurück auf den niederländischen Ingenieur und späteren Mathematiklehrer *Albert E. Bosman* (1891–1961). Er entwarf während des 2. Weltkrieges in seiner Freizeit an einem Zeichenbrett, an dem er sonst U-Boot-Pläne zeichnete, geometrische Muster. Seine Graphiken wurden 1957 in dem Buch *»Het wondere onderzoekingsveld der vlakke meetkunde«* veröffentlicht.

![Pythagoras-Baum](images/pythagorasbaum.jpg)

Der Pythagoras-Baum beruht auf einer rekursiven Abbildung des Pythagoras-Lehrsatzes: Die beiden Quadrate auf den Katheten des rechtwinkligen Dreiecks dienen als Verzweigung, auf dem jedes Kathetenquadrat sich wiederum verzweigt.

### Die Funktion drawPythagoras

Um die Funktion rekursiv aufrufen zu können, mußte ich sie aus der `draw()`-Funktion auslagern und sie in einen eigenen Aufruf packen:

~~~python
def drawPythagoras(a1, a2, b1, b2, level):
    if (level > 0):
        # Eckpunkte berechnen
        n1 = -b2 + a2
        n2 = -a1 + b1
        c1 = b1 + n1
        c2 = b2 + n2
        d1 = a1 + n1
        d2 = a2 + n2
        # Start-Rechteck zeichnen
        fill(palette[(level-1)%10])
        with beginClosedShape():
            vertex(a1 + xmitte, ymax - a2)
            vertex(b1 + xmitte, ymax - b2)
            vertex(c1 + xmitte, ymax - c2)
            vertex(d1 + xmitte, ymax - d2)
        e1 = d1 + w1*(c1 - d1) + w2*n1
        e2 = d2 + w1*(c2 - d2) + w2*n2
        # Schenkel-Quadrate zeichnen
        drawPythagoras(e1, e2, c1, c2, level-1)
        drawPythagoras(d1, d2, e1, e2, level-1)
~~~

Zum Zeichnen der einzelnen Quadrate habe ich nicht die `rect()`-Funktion genutzt, sondern *Shapes*, mit denen sich Punkte zu einem beliebigen Gebilde oder Polygon zusammefassen lassen. Hierzu müssen sie erst einmal mit `with beginClosedShape()` geklammert werden. Darin werden dann mit `vertex(x, y)` nacheinander die einzelnen Punkt aufgerufen, die (im einfachten Fall) durch Linien miteinander verbunden werden sollen. Mit `beginClosedShape` teile ich dem Sketch auch mit, daß das entstehende Polygon auf jeden Fall geschlossen werden soll, ein einfaches `with beginShape()` würde es offen lassen.

Der Aufruf ist rekursiv: Nachdem zuerst das Grundquadrat gezeichnet wurde, werden die rechten und die linken Schenkelquadrate gezeichnet, die dann wieder als Grundquadrate für den nächsten Rekursionslevel fungieren.

Processing (und damit auch der Python-Mode von Processing) ist gegenüber Rekursionstiefen realtiv robust. Die benutzte Rekursionstiefe von 12 wird klaglos abgearbeitet, auch Rekursionstiefen bis 20 sind -- genügend Geduld vorausgesetzt -- kein Problem. Bei einer Rekursionstiefe von 22 verließ mich aber auf meinem betagten MacBook Pro die Geduld.

### Die Farben

Für die Farben habe ich eine Palette in einer Liste zusammengestellt, die der Reihe nach die Quadrate einfärbt. Da die Liste nur 10 Elemente enthält, habe ich mit `fill(palette[(level-1)%10])` dafür gesorgt, daß nach 10 Leveln die Palette wieder von vorne durchlaufen wird.

### Der Quellcode

Da die eigentliche Aufgabe des Programms in die Funktion `drawPythagoras()` ausgelagert wurde, ist der restlich Quellcode von erfrischender Kürze:

~~~python
palette = [color(189,183,110), color(0,100,0), color(34,139,105),
           color(152,251,152), color(85,107,47), color(139,69,19),
           color(154,205,50), color(107,142,35), color(139,134,78),
           color(139, 115, 85)]

xmax = 600
xmitte = 300
ymax = 440

level = 12
w1 = 0.36   # Winkel 1
w2 = 0.48   # Winkel 2

def setup():
    size(640, 480)
    background(255)
    strokeWeight(1)
    noLoop()

def draw():
    drawPythagoras(-(xmax/10), 0, xmax/20, 0, level)

def drawPythagoras(a1, a2, b1, b2, level):
    if (level > 0):
        # Eckpunkte berechnen
        n1 = -b2 + a2
        n2 = -a1 + b1
        c1 = b1 + n1
        c2 = b2 + n2
        d1 = a1 + n1
        d2 = a2 + n2
        # Start-Rechteck zeichnen
        fill(palette[(level-1)%10])
        with beginClosedShape():
            vertex(a1 + xmitte, ymax - a2)
            vertex(b1 + xmitte, ymax - b2)
            vertex(c1 + xmitte, ymax - c2)
            vertex(d1 + xmitte, ymax - d2)
        e1 = d1 + w1*(c1 - d1) + w2*n1
        e2 = d2 + w1*(c2 - d2) + w2*n2
        # Schenkel-Quadrate zeichnen
        drawPythagoras(e1, e2, c1, c2, level-1)
        drawPythagoras(d1, d2, e1, e2, level-1)
~~~

Auch wenn es nicht nötig gewesen wäre, ich mag es einfach (und es dient der Übersichtlichkeit), wenn ich meine Processing.py-Sketche mit `def setup()` und `def draw()` gliedere. Mit `noLoop()` habe ich dann dafür gesorgt, daß die `draw()`-Schleife nur einmal abgearbeitet wird.

### Erweiterungen und Änderungen

Einen »symmetrischen« Pythagoras-Baum erhält man übrigens, wenn man die beiden Winkel-Konstanten `w1` und `w2` jeweils auf `0.5` setzt.

### Credits

Den rekursiven Algorithmus habe ich einem Pascal-Programm aus Jürgen Plate: *Computergrafik: Einführung – Algorithmen – Programmentwicklung*, München (Franzis) 2. Auflage 1988, Seiten 460-462 entnommen. Und die Geschichte des Baumes steht in dem schon mehrfach erwähnten Buch von Dieter Hermann, *Algorithmen für Chaos und Fraktale*, Bonn (Addison-Wesley) 1944 auf den Seiten 170f.


# Text(verarbeitung) in Processing.py

Mit `print()` oder `println()` kann man in Processing.py jede Ausgabe in das Konsolenfenster bringen, aber was ist, wenn der Text im Graphikfenster ausgegeben werden soll? Ich gehe erst einmal ganz naiv daran:

~~~python
font = None
tt = "Zwölf Boxkämpfer jagen Eva quer über den großen Sylter Deich."

def setup():
    size(800, 100)
    font = createFont("American Typewriter", 20)
    textFont(font)

def draw():
    background(255)
    fill(0)
    text(tt, 25, 50)
~~~

In der ersten Zeile teile ich Processing.py mit, daß ich die Variable `font` verwenden will und belege sie erst einmal mit dem Wert `none`. Das erspart mir ein oder sogar zwei Global-Statements. Die Stringvariable `tt` bekommt meinen Text zugewiesen. In `setup()` mache ich ein langes, schamles Fenster auf (mein Text ist ja ziemlich lang) und dann teile ich mit `createFont()` Processing.py mit, daß ich den Font *American Typewriter* in der Größe von 20 Pixeln verwenden will und weise ihn der Variablen `font` zu. Zu guter Letzt lege ich noch fest, daß eben mein textFont `font` ist.

In `draw()` lege ich einen weißen Hintergrund und eine schwarze Füllfarbe fest und lasse dann mit der Funktion `text()` den Text in das Fenster zeichnen. `text()` besitzt drei Parameter, zuerst den zu schreibenden (oder besser: zeichnenden) Text, dann die x- und die y-Koordinate des Textbeginns.

Das sieht eigentlich alles ganz einfach aus, aber wenn Ihr den Sketch ausführen lasst, erlebt Ihr Euer blaues Wunder:

![Screenshot](images/text01.jpg)

So verstümmelt habt Ihr Euch das sicher nicht vorgestellt. Die Ursache ist einfach und ärgerlich. Das Processing.py zugrundeliegende Python ist ein Jython (also die Java-Version von Python) und entspricht der Python-Version 2.7. Diese ist leider nicht *out of the box* UTF-8 fähig, ein Umstand, der in der (meist englischsprachigen) Literatur geflissentlich verschwiegen wird[^7_1]. Dabei ist er so leicht zu beheben. Ein vor einem String vorangestelltes `u` teilt Python 2.7 mit, daß dieser String ein UTF-8-String ist. Im Sketch ist also lediglich die Zeile

~~~python
tt = "Zwölf Boxkämpfer jagen Eva quer über den großen Sylter Deich."
~~~

in

~~~python
tt = u"Zwölf Boxkämpfer jagen Eva quer über den großen Sylter Deich."
~~~

und schon wird der Text wie gewünscht ausgegeben:

![Screenshot](images/text02.jpg)

Es gibt eine weitere, kleine Ungereimtheit im Umgang mit UTF-8 in Processing.py Im Haupt-Tab, in dem das ausführbare Programm steht (das ist der Tab, der die Endung `.pyde` bekommt), kann man -- wie gezeigt -- ohne große Probleme im Programmtext Umlaute unterbringen, während der Code in den anderen Tabs (die unter `.py` gespeichert werden) strenger mit dem Programmierer umgeht: Wenn nicht in der ersten Zeile

~~~python
# coding=utf-8
~~~

steht, meckert die IDE gnadenlos, selbst wenn Umlaute nur in den Kommentaren vorkommen.

[^7_1]: Ich weiß nicht, ob je und wann Jython den Sprung auf Python 3 wagt. Dort ist jedenfalls von Hause aus (per Default) jeder String ein UTF-8-String, in meinen Augen ein wichtiger, aber auch der einzige Grund, auf Python 3 umzusteigen.

>Der Text mit den zwölf Boxern ist übrigens ein [Pangramm](https://de.wikipedia.org/wiki/Pangramm), ein Satz, der alle Buchstaben des (in diesem Falle deutschen) Alphabets enthält. Früher wurden sie benutzt, um zum Beispiel Schreibmaschinen nach einer Reparatur zu testen. Heute nutze ich ihn, um festzustellen, ob ein Font auch alle Umlaute des deutschen Alphabets enthält. Das bekannteste englische Pangramm ist der Satz »The quick brown fox jumps over the lazy dog«.

### Als die Pangramme laufen lernten

Während in der Funktion `text()` die y-Koordinate immer die Grundlinie des Textes ist, kann man mit `textAlign()` festlegen, ob die x-Koordinate die rechte Kante (`RIGHT`), die linke Kante (`LEFT`) oder die Mitte (`CENTER`) des Textes betrifft. Das möchte ich ausnutzen, um eine Parade der Pangramme zu programmieren. Als erstes lege ich eine Liste mit Pangrammen an (der oben verlinkte Wikipedia-Artikel ist voll von ihnen). Und damit es auch ein wenig bunt wird, habe ich eine gleichlange Liste mit Farben zusammengestellt. Im Endeffekt soll das dann so aussehen:

![Screenshot](images/text03.jpg)

Der Sketch selber ist dadurch ein wenig länger geworden, aber das betrifft in der Hauptsache nur die beiden Listen:

~~~python
font = None
pangramme =
  [u"Zwölf Boxkämpfer jagen Eva quer über den großen Sylter Deich.",
   u"Jörg bäckt quasi zwei Haxenfüße vom Wildpony.",
   u"Falsches Üben von Xylophonmusik quält jeden größeren Zwerg.",
   u"Schweißgequält zündet Typograph Jakob verflixt öde Pangramme an.",
   u"Vom Ödipuskomplex maßlos gequält, übt Wilfried zyklisches Jodeln.",
   u"Asynchrone Bassklänge vom Jazzquintett sind nix für spießige Löwen."]
             
colors = ["#cd0000", "#008b00", "#ffff00", "#a52a2a", "#ff00ff", "#00ffff"]

def setup():
    global x, index
    frame.setTitle("Parade der Pangramme")
    size(800, 100)
    font = createFont("American Typewriter", 24)
    textFont(font)
    x = width
    index = 0

def draw():
    global x, index
    background(0)
    fill(colors[index])
    textAlign(LEFT)
    text(pangramme[index], x, 60)
    x -= 3
    w = textWidth(pangramme[index])
    if (x < -w):
        x = width
        index = (index+1) % len(pangramme)
~~~

Mit `textAlign(LEFT)` und `x = width` habe ich festgelegt, daß der Text im ersten Schritt am rechten Fensterrand beginnt und quasi ins Leere geschrieben wird. Bei jedem Durchlauf wird `x` umd drei dekrementiert und so beginnt das erste Pangramm von rechts nach links durch das Fenster zu scrollen. Ist der Text aus dem sichtbaren Bereich des Fenster verschwunden (`x < -w`), dann wird `index` um einen erhöht und das nächste Pangramm beginnt seine Parade. Damit der Index nicht irgendwann überläuft wird er Modulo der Länge der Liste der Pangramme berechnet. Und da ich in weiser Voraussicht die Länge der Farbliste gleich der Länge der Liste der Pangramme entworfen habe, passiert auch bei den Farben nichts.

### Font, Font, Font

Jetzt bleibt nur noch eins zu tun. Auf meinem Rechner läuft der Sketch ohne Probleme, da ich weiß, daß auf meinen Rechner der Font *American Typewriter* vorhanden ist. Dies muß aber nicht auf jedem anderen Rechner der Fall sein (falls also bei Euch die Sketche nicht laufen, tauscht einfach *American Typewriter* mit einem anderen Font, der auf Eurem Rechner vorhanden ist, aus). Wenn ich die `.ttf`-Datei des Fonts in den `data`-Ordner des Sketches kopiere (das geht am einfachsten, wenn ich die Datei auf das Editor-Fenster der IDE schiebe), würde der Sketch -- wenn ich ihn weitergebe -- überall funktionieren. Aber *American Typewriter* unterliegt mit Sicherheit dem Urheberrecht und eine Weitergabe ist vermutlich verboten oder mit hohen Kosten verbunden.

Aber es gibt ja eine Menge freier Fonts im Web und die größte Quelle dieser freien Fonts ist [Google Fonts](https://fonts.google.com/). Dort habe ich mir den Font [Barrio](https://fonts.google.com/specimen/Barrio) heruntergeladen, der unter der [Open Font Licence](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web) zu nutzen ist.

![Screenshot](images/text04.jpg)

Selbstverständlich habe ich mich vorher vergewissert, daß der Font auch die von mir gewünschten deutschen Umlaute enthält. Nachdem ich die Fontdatei dem Sketch hinzugefügt hatte, war eigentlich nur noch eine Zeile im Programm zu ändern:

~~~python
    font = createFont("Barrio-Regular.ttf", 64)
~~~

*Barrio* ist ein Display-Font, der nur ab einer gewissen Größe wirkt. Daher habe ich ihn auf `64` gesetzt und dann die y-Koordinate etwas weiter nach unten geschoben. Der vollständige und endgültige Sketch der Pangramm-Parade sieht daher nun so aus:

~~~python
font = None
pangramme =
 [u"Zwölf Boxkämpfer jagen Eva quer über den großen Sylter Deich.",
  u"Jörg bäckt quasi zwei Haxenfüße vom Wildpony.",
  u"Falsches Üben von Xylophonmusik quält jeden größeren Zwerg.",
  u"Schweißgequält zündet Typograph Jakob verflixt öde Pangramme an.",
  u"Vom Ödipuskomplex maßlos gequält, übt Wilfried zyklisches Jodeln.",
  u"Asynchrone Bassklänge vom Jazzquintett sind nix für spießige Löwen."]
             
colors = ["#cd0000", "#008b00", "#ffff00", "#a52a2a", "#ff00ff", "#00ffff"]

def setup():
    global x, index
    frame.setTitle("Parade der Pangramme")
    size(800, 100)
    font = createFont("Barrio-Regular.ttf", 64)
    textFont(font)
    x = width
    index = 0

def draw():
    global x, index
    background(0)
    fill(colors[index])
    textAlign(LEFT)
    text(pangramme[index], x, 80)
    x -= 3
    w = textWidth(pangramme[index])
    if (x < -w):
        x = width
        index = (index+1) % len(pangramme)
~~~

Wenn Ihr noch mehr über Strings, Text und Fonts in Processing.py wissen wollt, *Daniel Shiffman* hat dazu ein [nettes Tutorial](http://py.processing.org/tutorials/text/) verfaßt, daß auch mir bei meinen Erkundungen sehr geholfen hat.

## UTF-8-Text aus Dateien lesen

![Screenshot](images/boxerscreenshot.jpg)

In der Reference für Processing 3 steht bei allen Datei-Operationen, [so auch bei `loadStrings()`](https://processing.org/reference/loadStrings_.html):

>*Starting with Processing release 0134, all files loaded and saved by the Processing API use UTF-8 encoding. In previous releases, the default encoding for your platform was used, which causes problems when files are moved to other platforms.*

Das ließ hoffen, daß man in Processing.py wenigstens an dieser Stelle ohne das (von mir) ungeliebte `u"utf-8-string"` auskommen kann. Das wollte ich ausprobieren, also legte ich mir als erstes eine (UTF-8-) Textdatei mit diesem Inhalt an:

![Screenshot](images/boxertext01.jpg)

Das sieht doch schon sehr gefährlich aus, in der ersten Zeile die bösen deutschen Umlaute, die zweite Zeile mit japanischen Schriftzeichen, die dritte enthält chinesische Glyphen und die letzte Zeile kyrillische (russische) Zeichen. Noch vor wenigen Jahren hätte das jeden Programmierer an den Rand des Wahnsinns gebracht, aber nun: Selbst dieser simple Dreizeiler

~~~python
lines = loadStrings("boxer.txt")
for line in lines:
    print(line)
~~~

gibt den Text mit allen Sonderzeichen auf der Konsole aus. Und auch der Befehl `text(line, x, y, w, h)` hat keine Schwierigkeiten (einen UTF-8-fähigen Font vorausgesetzt) diesen Text in das Processing-Fenster zu zaubern. Hier das Progrämmchen, das obigen Screenshot produziert:

~~~python
font = None

def setup():
    size(500, 500)
    # fontList = PFont.list()
    # printArray(fontList)
    font = createFont("Palatino-Roman", 32)
    textFont(font)
    noLoop()

def draw():
    background(30)
    textSize(32)
    u = 50
    text("Seltsame Zeichen", 20, u)
    u = 80
    textSize(24)
    lines = loadStrings("boxer.txt")
    for line in lines:
        print(line)
        text(line, 20, u, 460, 500)
        u += 80
~~~

Die beiden auskommentierten Zeilen listen in der Konsole alle auf dem System verfügbaren Fonts auf, mit dem Namen, in dem sie mit `createFont()` in Processing angesprochen werden können. Wenn man einen dieser Fonts verwendet, erspart das zwar einerseits die Installation eines Fonts im `data`-Ordner, macht aber auf der anderen Seite solch ein Skript weniger portabel, denn was ist, wenn der Empfänger diesen Font nicht installiert hat.

### Keine Emojis

In einer ersten Version des Textes hatte ich auch noch ein paar Emojis hineingeschmuggelt. Hier wurde aber eine Grenze überschritten, Emojis wurden weder in der Konsole noch auf dem Canvas angezeigt (man kann sie auch nicht per *Copy & Paste*) in den Editor schmuggeln`. Das gilt aber auch für den Java-Mode von Processing, Emojis sind erst ab P5.js in der Welt von Processing vorgesehen.

### Caveat

Auch wenn ich es natürlich schön finde, daß das ungeliebte `u"utf-8-string"` bei den Dateioperationen mit Processing-Befehlen wegfällt, ist es natürlich inkonsistent. Denn Dateioperationen mit Python-Befehlen arbeiten natürlich weiterhin mit der besonderen UTF-8-Kodierung von Python 2.7, so zum Beispiel die Befehle um CSV- oder JSON-Dateien zu lesen und zu schreiben. Daher ist eine gewisse Vorsicht angebracht.


## Spaß mit Processing.py: Rentenuhr

Was für Gründe sprechen eigentlich dafür, Processing.py statt des »normalen« Processings zu nutzen? Nun, zum einen können es persönliche Gründe sein: Ich mag zum Beispiel keine Programmiersprachen, die Blöcke mit geschweiften Klammern (`{}`) trennen und vermeide sie, wo es nur geht. Zum anderen komme ich aus der [Pascal](http://cognitiones.kantel-chaos-team.de/programmierung/pascal.html)-Ecke (Pascal und Algol 68 waren meine ersten Programmiersprachen überhaupt) und mag daher Programme, die so etwas sind wie »ausführbarer Pseudocode«. Aber der wichtigste Grund ist, Processing.py ist eben nicht nur Processing, sondern auch Python. Und Python kommt *»batteries included«*, es bringt eine große Anzahl von Standard-Bibliotheken mit, die man auch in Processing.py nutzen kann. Ich möchte das am Beispiel des Python-Moduls `datetime` einmal zeigen:

![Screenshot](images/rentenuhr.jpg)

Als erstes habe ich den freien ([Open Font Licence](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web)) Font [Coda Heavy](https://fonts.google.com/specimen/Coda) von Googles Seiten heruntergeladen, entpackt und ihn dem Skript zugänglich gemacht, indem ich die `.ttf`-Datei einfach auf das IDE-Fenster geschoben habe. Processing legt dann automatisch im Skriptordner ein `data`-Vertzeichnis an und kopiert die Datei -- wie auch alle Bild- oder Audio-Datein dorthin. Die Skripte finden sie dann, zum Beispiel mit

~~~python
	font = createFont("Coda-Heavy.ttf", 96)
~~~

ohne eine spezielle Pfadangabe. Der zweite Parameter gibt die maximale Fontgröße vor. Am Anfang des Skriptes habe ich mit

~~~python
	import datetime as dt
~~~

das Python-Modul `datetime` aus der Standardbibliothek geladen und dann als erstes eine einfache Uhr gebastelt

~~~python
	myNow = dt.datetime.now()
	myHour = str(myNow.hour)
	myMinute = str(myNow.minute)
	mySecond = str(myNow.second)
~~~

und dann die `datetime`-Objekte in Strings verwandelt. Im eigentlichen Programm habe ich sie sogar noch ein wenig aufgehübscht und den einstelligen Sekunden und Minute eine führende Null verpaßt. Das könnt Ihr weiter unten im kompletten Quellcode nachlesen.

Jetzt kommt aber der eigentliche Gag: Mit den `datetime`-Objekten kann man nämlich rechnen! Und da ich am 31. Dezember 2018 in Rente gehe, wollte ich wissen, wieviele Tage ich noch ausharren muß

~~~python
    rente = dt.date(2018, 12, 31)
    heute = dt.date.today()
    differenz = rente - heute
    myDays = str(differenz.days)
    workingDays = float(myDays)/7.0 * 5
    workingDays = str(int(workingDays - 80))
~~~

und wieviele Tage davon Arbeitstage sind. Dazu habe ich einfach die Anzahl der Tage durch sieben geteilt und mit fünf multipliziert, was grob die Anzahl der Werktage ergibt. Und da ich noch 20 Tage Resturlaub in dieses Jahr mitgeschleppt habe und mir pro Jahr auch noch je 30 Tage regulärer Urlaub zusteht, habe ich diese 80 Tage auch noch abgezogen. Die Feiertage habe ich nicht berücksichtigt, mir reicht diese grobe Schätzung.

Da die Differenz zweier `datetime`-Objekte wieder ein `datetime`-Objekt ist, muß die Umwandlung in einen *String* explizit mittels *Typecasting* vorgenommen werden und bei der Division durch sieben ist zu beachten, daß das Processing.py zugrundelegende Jython ein Python 2.7 ist und deshalb bei einer Integer-Division alle Nachkommastellen abschneidet (zum Beispiel ergibt `13/7` eine `1`, dieses -- dokumentierte -- Verhalten wurde in Python 3 geändert). Um das zu vermeiden, habe ich durch `7.0` geteilt und so eine Float-Division erzwungen und durch ein anschließendes Runden das Ergebnis doch wieder in eine Integer-Zahl verwandelt.

Jetzt das komplette Skript zum Nachlesen und Nachprogrammieren:

~~~python
import datetime as dt

def setup():
    size(640, 480)
    font = createFont("Coda-Heavy.ttf", 96)
    textFont(font)

def draw():
    background("#000000")
    myNow = dt.datetime.now()
    myHour = str(myNow.hour)
    myMinute = str(myNow.minute).rjust(2, "0")
    mySecond = str(myNow.second).rjust(2, "0")
    myTime = myHour + " : " + myMinute + " : " + mySecond
    textSize(96)
    text(myTime, 60, 150)
    rente = dt.date(2018, 12, 31)
    heute = dt.date.today()
    differenz = rente - heute
    myDays = str(differenz.days)
    workingDays = float(myDays)/7.0 * 5
    workingDays = str(int(workingDays - 80))
    myText = u"Lieber Jörg, es sind nur noch " + myDays + \
    u" Tage bis zu Deiner Rente!\nDas sind etwa " + \
    workingDays + " Arbeits- tage. Das schaffst Du!"
    textSize(32)
    text(myText, 60, 200, 540, 300)
~~~

Wegen des Umlautes in meinem Vornamen, mußte ich mit `u"…"` die Umwandlung des Strings in einen UTF-8-String erzwingen (auch das ist Python 3 nicht mehr nötig), aber wie der obige Screenshot zeigt, wird dann der Umlaut auch brav angezeigt.

Die Funktion `text()` kann man in Processing einmal mit drei und einmal mit fünf Parametern aufrufen. Im ersten Fall übergibt man den Text und die x- und y-Koordinaten der linken Grundlinie des Textes. Im zweiten Fall kommen noch die Weite und die Höhe der Textbox hinzu. Damit erreicht man, daß ein langer String an den Textbox-Grenzen umgebrochen wird und der Text nicht aus dem Fenster herausläuft. Die Parameter habe ich durch einfaches Ausprobieren bekommen.


# Bildverarbeitung mit Processing.py

### Jeder sein kleiner Warhol

Processing und damit auch Processing.py besitzt ein ganzes Arsenal von Filtern zur Bildmanipulation. Davon möchte ich zu Beginn zwei heraussuchen und damit ein kleines Programm erstellen, dessen Ergebnis ein wenig an die berühmten Siebdrucke des Pop-Art-Künstlers [Andy Warhol](https://de.wikipedia.org/wiki/Andy_Warhol) erinnern soll.

![Warhol like](images/warhollike.jpg)

Ich habe dazu ein Photo von unserem Sheltie Joey und mir genommen, das *Stefanie Radon* vor etwa vier Jahren von uns geschossen hatte, und das mein Facebook-Profil ziert und mit dem `filter(THRESHOLD, 0.55)` in eine reine schwarz-weiß-Zeichnung umgewandelt. `THRESHOLD` akzeptiert Parameter zwischen `0.0` und `1.0` -- je kleiner der Wert, desto weniger wird angezeigt. Nach einigen Experimenten habe ich mich dann auf `0.55` festgelegt, das brachte in meinen Augen das brauchbarste Ergebnis für dieses Photo.

In der `draw()`-Funktion habe ich dann das Bild acht mal hintereinander in zwei Reihen gezeichnet und mit dem filter `tint(color)` jeweils in einer anderen Farbe eingefärbt. Ich habe einige Zeit mit den Farben experimentieren müssen, bis ich das oben angezeigt Ergebnis bekam, mit dem ich nun zufrieden bin.

### Der Quellcode

Der Quellcode ist einfach und leicht zu verstehen. Im `setup()` habe ich das Bild geladen und in eine schwarz-weiß-Version umgewandelt, in `draw()` habe ich dann die acht unterschiedlich eingefärbten Versionen erstellt. Dabei habe ich eine Schleife über die Liste `palette[]` der von mir ausgewählten Farben laufen lassen:

~~~python
palette = [color(205, 133, 63), color(124, 205, 124),
           color(255, 140, 0), color(255, 20, 147),
           color(238, 238, 0), color(224, 102, 255),
           color(151, 255, 255), color(205, 200, 177)]

def setup():
    global jojo
    size(640, 320)
    jojo = loadImage("jojo.jpg")
    jojo.filter(THRESHOLD, 0.55)
    noLoop()

def draw():
    global jojo
    background(51)
    for i in range(len(palette)):
        if (i < 4):
            row = 0
            j = i
        else:
            row = 160
            j = i - 4
        tint(palette[i])
        image(jojo, j*160, row)
~~~

### Ressourcen

Natürlich könnt Ihr für Eure eigenen Experimente auch das Photo von [Joey und mir](https://www.flickr.com/photos/schockwellenreiter/7780799276/) nutzen -- es steht schließlich auf Flickr und im Fratzenbuch, aber es wäre sicher mehr im Sinne von Andy Warhol, wenn Ihr Euch Eure eigene Bilder (aus-) sucht, die Ihr einfärben und serialisieren wollt.


## Filter für die Bildverarbeitung

Processing und damit auch Processing.py bringen eine kleine Sammlung vorgefertigter Filter für die Bildmanipulation mit, die auf jedes Bild angewandt werden können. Die Filter haben folgende Syntax: Entweder

~~~python
filter(MODE)
~~~

oder

~~~python
filter(MODE, param)
~~~

Ob ein Filter einen zusätzlichen Paramter mitbekommen kann, hängt vom Filter ab. Wie die Filter wirken und ob und wie sie einen Paramter mitbekommen, könnt Ihr der folgenden Tabelle entnehmen:

----------------------------------------------------------------------------------
Ergebnis                   Filter
-------------------------- -------------------------------------------------------
![](images/filter0200.jpg) Originalbild (keinen Filter)    

![](images/filter0201.jpg) `THRESHOLD`, Parameter (optional) zwischen 0 und 1, Default 0.5                         
-----------------------------------------------------------------------------------

Table: Filter in Processing

Mit folgendem kleinen Sketch könnt Ihr mit den diversen Filtern spielen (die auskommentierten Teile habe ich für die *Thumbnails* in obiger Tabelle benötigt):

~~~python
selectFilter = 8

def setup():
    global img
    # Thumbnails
    # size(160, 120)
    # img = loadImage("abendrot-s.jpg")
    # Volle Größe
    size(640, 480)
    img = loadImage("abendrot.jpg")
    noLoop()

def draw():
    global img
    background(255, 127, 36)
    image(img, 0, 0)
    if (selectFilter == 1):
        filter(THRESHOLD, 0.55)
    elif (selectFilter == 2):
        filter(GRAY)
    elif (selectFilter == 3):
        filter(INVERT)
    elif (selectFilter == 4):
        filter(POSTERIZE, 4)
    elif (selectFilter == 5):
        filter(BLUR, 6)
    elif (selectFilter == 6):
        filter(ERODE)
    elif (selectFilter == 7):
        filter(DILATE)
    elif (selectFilter == 8):
        filter(GRAY)
        filter(POSTERIZE, 4)
    # save("filter020" + str(selectFilter) + ".jpg")
~~~

Einfach bei `selectFilter` den gewünschten Wert (zwischen `0` und `8`) eingeben und dann den Sketch laufen lassen. Ihr seid natürlich eingeladen, bei den Filtern, die Parameter zulassen, mit diesen zu spielen.

Die letzte (auskommentierte) Zeile zeigt Euch, wie Ihr das Ergebnis abspeichern könnt. Das Format des Bildes erkennt Processing an der Endung.

### Filter interaktiv

![Screenshot](images/posterize.jpg)

Noch besser könnt Ihr natürlich die Wirkung der diversen Filterparameter interaktiv mit der Maus erkunden. Ich habe als Beispiel dafür zwei kleine Sketche geschrieben, die einmal `POSTERIZE` und zum anderen `THRESHOLD` erkunden.

~~~python
def setup():
    global img
    size(640, 480)
    frame.setTitle("Posterize interaktiv")
    img = loadImage("abendrot.jpg")

def draw():
    v = map(mouseX, 0, width, 2, 64)
    image(img, 0, 0)
    filter(POSTERIZE, v)
~~~

Da die hohen Werte bei `POSTERIZE` keinen interessanten Effekte mehr liefern, habe ich hier mithilfe der `map()`-Funktion den Parameter auf die Werte zwischen `2` und `64` begrenzt.

~~~python
def setup():
    global img
    size(640, 480)
    frame.setTitle("Threshold interaktiv")
    img = loadImage("abendrot.jpg")

def draw():
    v = float(mouseX)/width
    image(img, 0, 0)
    filter(THRESHOLD, v)
~~~

`THRESHOLD` erwartet Werte zwischen `0.0` und `1.0`. Daher habe ich einfach den `mouseX`-Wert durch die Breite des Fensters geteilt. Wegen der Integer-Division von Python 2.7 mußte ich einen der Werte explizit zu einem `float` konvertieren, um das gewünschte Ergebnis zu erhalten (denn sonst bekommt man nur den Wert Null). So aber wird das Bild, wenn die Maus ganz weit links ist, nur weiß, während es bei einer Mausposition ganz rechts im Fenster fast vollständig schwarz wird. Irgendwo dazwischen liegen die interessanten Ergebnisse. Ihr solltet dies mit diversen Bildern ausprobieren, um ein Gefühl für die zu erwartenden Effekte zu bekommen.

## Pointillismus

[Pointillismus](https://de.wikipedia.org/wiki/Pointillismus) bezeichnet eine Stilrichtung der Malerei, die zwsichen 1889 und 1910 ihre Blütezeit hatte. Pointillistische Bilder bestehen aus kleinen regelmäßigen Farbtupfern in reinen Farben. Der Gesamt-Farbeindruck einer Fläche ergibt sich erst im Auge des Betrachters und aus einer gewissen Entfernung. So etwas in der Art kann man natürlich auch leicht in Processing.py nachbilden (wobei die möglichst reinen Farben in dem Beispielprogramm nur annähernd getroffen werden, weil es sich bei dem Ausgangsbild um eine handkolorierte Photographie vermutlich ebenfalls aus dem 19. Jahrhundert handelt[^8_1]).

[^8-1]: Fragt nicht, wo ich diese Photographie gefunden habe. Ich habe sie einfach aus den unendlichen Tiefen des WWW gefischt.

![Nachkolorierter Akt](images/screenshotfarbakt02.jpg)

Das Programmfenster zeigt links das Ausgangsbild. Rechts entsteht so langsam das aus Kreisen zufälliger Größe zusammengesetzte Zielbild. Dabei besitzen die Punkte einen Ausganswert (`radius`) von sechs, der mit einem Zufallsfaktor zwischen 0.2 und 1.5 multipliziert wird. (Ich benutze im Programm die `randint()`-Funktion von Python und nicht die eingebaute `random()`-Funktion von Processing. Mir ist die Python-Funktion irgendwie sympathischer, aber das ist vermutlich Geschmackssache.)

Bei jedem Durchlauf der `draw()`-Schleife wird der Farbwert eines zufälligen Punktes im Ursprungsbild ermittelt und dann als Kreis (Punkt) im Zielbild eingezeichnet. Das Ergebnis gleicht dem Ursprungsbild, nur das es den Anschein erweckt, als würde man es durch eine Scheibe Strukturglas, wie sie manchmal Duschen- oder Badezimmertüren zieren, betrachten.

## Der Quellcode

~~~python
import random as r
radius = 6

def setup():
    global akt
    size(800, 640)
    akt = loadImage("akt.jpg")
    background(0)
    frameRate(600)

def draw():
    global akt
    image(akt, 0, 0)
    x = r.randint(0, akt.width - 1)
    y = r.randint(0, akt.height - 1)
    c = akt.pixels[x + y*akt.width]
    zufall = r.randint(2, 15)/10.0
    noStroke()
    fill(c)
    ellipse(x + 400, y, radius*zufall, radius*zufall)
~~~

Der Quellcode ist wieder schön kurz und lädt zum Experimentieren ein. Setzt man zum Beispiel die Konstante `radius = 3`, dann wirkt das Zielbild bedeutend realistischer. Und ein sehr seltsames Ergebnis bekommt man, wenn man die Zeile mit dem `noStroke()` auskommentiert.

Man muß natürlich nicht unbedingt Kreise zeichnen. Ein Quadrat oder ein Dreieck ergibt noch ganz andere Effekte. Spielt einfach mal ein wenig damit herum. Processing(.py) ist zum Spielen entworfen worden.

## Noch mehr Pointillismus

Wenn ich ehrlich bin, kann das Ergebnis des Programms aus dem letzten Abschnitt weder ästhetisch noch im Sinne des Pointillismus wirklich überzeugen. Das liegt daran, daß im Programm jedes einzelne Pixel befragt und dann als vergrößerter Punkt wiedergegeben wird. So entsteht im Endeffekt so etwas wie ein verwaschenes Original, aber kein Raster. Daher habe ich -- nach einer Idee aus dem wunderbaren Buch »Generative Gestaltung« (derzeit leider nur auf englisch verfügbar) -- tatsächlich eine Rasterversion des Aktbildes programmiert und das Ergebnis überzeugt mich mehr:

![Screenshot](images/akt2.jpg)

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

### Der Quellcode

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

# Animationen

## Ein kleiner roter Luftballon

# Spaß mit (SVG-) Shapes: Pinguine im Eismeer

# Objkete und Klassen mit Kitty

## Hallo Hörnchen – Hallo Kitty revisited

## Moving Kitty

## Klasse Kitty!

## »Cute Planet« mit Processing.py

## Fluffy Planet

# Zelluläre Automaten

## Das Demokratie-Spiel

## Frösche und Schildkröten oder: Wie entsteht Segregation?

## Der Waldbrand-Simulator

# 3D mit Processing.py

## Kugeln und Kisten

## Und es geht doch: Kugeln und Texturen

## Die Erde ist eine Kiste

## Licht und Schatten

## Einen Globus basteln

# Einen eigenen Wetterbericht mit OpenWeatherMap

# WordCram: Processing.py und eine Processing (Java) Bibliothek

# Running Orc mit Processing.py

## Running Orc in vier Richtungen

## Ork mit Kollisionserkennung

## Ein Ork im Labyrinth

## Der autonome Ork

## Drei Orks und ein Held

# Exkurs Rauhnächte: Spaß mit Processing.py

# Exkurs: Walking Pingus

# Das Avoider Game

## Game Stage 1

## Stage 2

## Stage 3: Sternenhimmel

## Stage 4: PowerUp und PowerDown

## Nachtrag: Avoider Game Stage 4a

# Epilog

# Anhang

## Literaturverzeichnis

## Index