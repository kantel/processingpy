# Die Erde ist eine Kiste

Natürlich kann man das, was ich [hier](http://py.kantel-chaos-team.de/kugel02/) mit einer Kugel angestellt habe, auch mit einer Kiste (in Processing `BOX` genannt) anstellen. Der einzige Unterschied ist, daß die Textur jeweils komplett auf alle sechs Seiten der Box abgebildet wird.

[![Screenshot](images/kiste.jpg)](https://www.flickr.com/photos/schockwellenreiter/33011293496/)

Aber dann hat man den Beweis: Die Erde ist eine Kiste!

## Quellcode

~~~python
a = 0

def setup():
    global chest
    earth = loadImage("bluemarble.jpg")
    size(400, 400, P3D)
    noStroke()
    chest = createShape(BOX, 180)
    chest.setTexture(earth)

def draw():
    global a, chest
    background(51)
    lights()
    translate(width*.5, height*.5, 0)
    sphereDetail(30)
    with pushMatrix():
        rotateZ(radians(frameCount))
        rotateX(radians(frameCount*.5))
        rotateY(radians(a))
        a += 0.01
        shape(chest)
~~~