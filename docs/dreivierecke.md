# Geometrische Grundformen

Processing besitzt ein kleines Set von geometrischen Primitiven in 2D (im Englischen *Shapes* genannt) mit denen sich so einiges anstellen läßt. Neben den schon bekannten Punkten und Kreisen und Ellipsen, gibt es noch einige andere, die ich der Reihe nach vorstellen möchte:

[![Screenshot](images/shapes.jpg)](https://www.flickr.com/photos/schockwellenreiter/32867269721/)

## Rechtecke

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

## Kreise und Ellipsen

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

## Dreieck

Das Dreieick ist eines der einfachsten geometrischen Grundformen in Processing. Es existiert nur in der Form

~~~python
triangle(x1, y1, x2, y2, x3, y3)
~~~

und hat auch keinen besonderen Mode. Die jeweiligen x- und y-Koordinagen sind die Koordinaten des ersten, zweiten und dritten Punktes. Bei der Reihenfolge wird -- oben beginnend -- immer im Uhrzeigersinn vorgegangen. Das ist alles.

## Unregelmäßige Vierecke

Ähnlich einfach verhält es sich mit den unregelmäßigen Vierecken. Sie werden mit

~~~python
quad(x1, y1, x2, y2, x3, y3, x4, y4)
~~~

erzeugt und auch hier sind es absolute Koordinaten und das Gebilde besitzt ebenfalls keinen besonderen Mode. Auch hier wird bei der Zählung links oben begonnen und dann werden die Ecken ebenfalls im Uhrzeigersinn abgearbeitet.

## Kreisbögen

Kreisbögen sind mit der Ellipse (genauer: dem Kreis verwandt) und besitzen die gleichen Modi wie diese (mit dem gleichen Default `CENTER`). Sie werden wie folgt aufgerufen:

~~~python
arc(x, y, w, h, start, stop)
arc(x, y, w, h, start, stop, mode)
~~~

Die x- und y-Koordinaten sind im Default-Mode der Mittelpunkt des Kreises, während `w` und `h` im Default-Mode die Breite und Höhe des Kreisen angeben. `start` und `stop` sind die Winkel (in *radians*) für die Länge des Kreisbogens.

Dann gibt es hier noch einen besonderen `mode`. Der kann `OPEN` (das ist der Default), `CHORD` oder `PIE` heißen. Im Default `OPEN` bleibt der Kreisbogen offen, falls es jedoch ein `fill()` gibt, wird er dennoch gefüllt. Bei `CHORD` wird der Kreisbogen geschlossen und bei `PIE` bildet er ein Kuchenstück, wie man es von Tortengraphiken kennt.


## Der Quelltext

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

## Credits

Teilweise folgt dieser Sketch einer Idee von *Jan Vantomme* aus seinem Buch»[Processing 2: Creative Coding Programming Cookbook][amazon]« (Seiten 31 ff.). Ich habe sie abgewandelt, die Beispiele für die Kreisbögen hinzugefügt und vom Java-Mode in den Python-Mode übertragen.



[amazon]: https://www.amazon.de/Processing-2-Creative-Programming-Cookbook/dp/1849517940/ref=as_li_ss_tl?ie=UTF8&qid=1487522332&sr=8-1&keywords=Processing+2:+Creative+Programming+Cookbook&linkCode=ll1&tag=derschockwell-21&linkId=883652024ea3cb5c1944e15a7f3b957f