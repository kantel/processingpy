# Breakout (Standard-Version)

In diesem zweiten, größeren Projekt möchte ich alles zusammenbringen, was bisher über Shapes, Animationen und Kollisionen behandelt wurde. Ich möchte dafür zuerst das klassische [Breakout-Spiel](https://de.wikipedia.org/wiki/Breakout_(Computerspiel)), ursprünglich ein Spielhallenklassiker, der in vielen Formen für viele Heimcomputer nachprogrammiert wurde, in Processing.py erstellen. Danach möchte ich eine Variation vorstellen, die jüngst *Yining Shi* als Gastdozentin bei *Daniel Shiffman* in P5.js, dem JavaScript-Mode von Processing, vorgestellt hat. Aber fangen wir erst einmal bei den Basics an:

## Paddle and Ball

Das Spiel, das man auch als eine Solo-Variante von [Pong](https://de.wikipedia.org/wiki/Pong) sehen kann benötigt erst einmal einen *Paddle*, der mit den Pfeiltasten hin- und herbewegt werden kann und mit dem der Spieler verhindern soll, daß der Ball, der die *Bricks* treffen und damit zum Verschwinden bringen soll, nach unten ins Nirwana fällt. Denn fällt der Ball nach unten, hat der Spieler in der einfachsten Version verloren. Es gibt auch Versionen, in denen der Spieler mehrere Bälle hat und erst, nachdem er den letzten Ball nicht mehr mit dem *Paddle* zurückschlagen konnte, war das Spiel zu Ende.

Gewonnen hatte der Spieler, wenn er alle *Bricks* mit dem Ball weggeschlagen hat. Das ist nicht einfach, weil nicht jeder Stein verschwindet, wenn er getroffen wird. Manche Steine müssen zwei- oder dreimal getroffen werden, bevor ie verschwinden.

Setzen wir erst einmal unsere Spielwelt auf:

~~~python
def setup():
    size(605, 400)

def draw():
    background(0, 0, 0)
~~~

Da passiert noch nicht viel, alles was wir haben, ist ein schwarzes Fenster. Die benötigten Klassen lade ich der Übersicht halber in eine separate Datei (einen separaten Tab) aus, den ich `gameworld.py` genannt habe. Dort wird als erstes die Klasse `Paddle` erstellt:

### Paddle

~~~python
# coding=utf-8

class Paddle(object):

    def __init__(self):
        self.w = 120
        self.h = 15
        self.pos = PVector(width/2 - self.w/2, height - 40)
        self.isMovingLeft = False
        self.isMovingRight = False
        self.stepSize = 20

    def display(self):
        fill("#ff9664")
        noStroke()
        rect(self.pos.x, self.pos.y, self.w, self.h)

    def update(self):
        if self.isMovingLeft:
            self.move(-self.stepSize)
        elif self.isMovingRight:
            self.move(self.stepSize)

    def move(self, step):
        self.pos.x += step

    def checkEdges(self):
        if self.pos.x <= 0:
            self.pos.x = 0
        elif self.pos.x + self.w >= width:
            self.pos.x = width - self.w
~~~

Der Konstruktor legt die Größe des Paddles fest und initialisiert seine Position ungefähr in die Mitte des Fensters und 40 Pixel oberhalb des unteren Randes. Außerdem werden die boolschen Variabeln `isMovingLeft` und `isMovingRight` auf `False` gesetzt. Die Funktionen `display()`, `update()` und `checkEdges()` werden vom Hauptprogramm benötigt, `move()` hingegen wird nur intern von `update()` aufgerufen. `display()` macht nichts anderes, als die Farbe für das *Paddle* festzulegen und an der aktuellen Position ein Rechteck zu zeichnen, `update()` bewegt das *Paddle* je nach Zustand der boolschen Variablen `isMovingRight` oder `isMovinLeft` mit Hilfe der `move()`-Funktion entweder nach rechts oder nach links. Sind beide boolschen Variablen `False`, dann bewegt sich das *Paddle* eben nicht.

`checkEdges()` sorgt dafür, daß das *Paddle* das Fenster nicht verläßt, sondern an der rechten oder linken Seite gestoppt wird.

Um das ganze in Action zu sehen, müssen wir das Hauptprogramm erweitern:

~~~python
from gameworld import Paddle

def setup():
    global paddle
    size(605, 400)
    paddle = Paddle()

def draw():
    global paddle
    background(0, 0, 0)
    paddle.display()
    paddle.checkEdges()
    paddle.update()
    
def keyReleased():
    global paddle
    paddle.isMovingRight = False
    paddle.isMovingLeft = False

def keyPressed():
    global paddle
    if key == CODED:
        if keyCode == LEFT:
            paddle.isMovingLeft = True
        elif keyCode == RIGHT:
            paddle.isMovingRight = True
~~~

Erst einmal wird natürlich die Klasse `Paddle` importiert und in `setup()` eine Instanz von Paddle erzeugt. Die `draw()`-Schleife zeigt das *Paddle* erst einmal an, püft dann, ob es an eine Ecke stößt und führt anschließend die `update()`-Funktion aus. Dazu müssen wir noch die Tasteneingaben abfragen. `keyPressed()` setzt in Abhängigkeit davon, ob die rechte oder linke Pfeiltaste gedrückt wurde, entweder`isMovingLeft` oder `isMovingRight` auf `True`. Sobald die Taste aber wieder losgelassen wird, setzt `keyReleased` alles wieder auf `False`.

Das kann jetzt getestet werden und das *Paddle* bewegt sich brav nach rechts oder links, wenn eine der Pfeltasten gedrückt wird.

### Der (Bouncing) Ball

Als nächstes werde ich den *Ball* implementieren, erst einmal zu Testzwecken als *Bouncing Ball*, der von allen vier Seiten reflektiert wird. Die untere Seite werde ich später auskommentieren, damit der Ball ins Nirwana entschwinden kann, aber vorerst sieht die Klasse `Ball` (in `gamewolrd.py`) so aus:

~~~python
class Ball(object):
    
    def __init__(self):
        self.r = 10
        self.vel = PVector(1, 1)*4
        self.dir = PVector(1, 1)
        self.pos = PVector(width/2, height/2)
    
    def update(self):
        self.pos.x += self.vel.x*self.dir.x
        self.pos.y += self.vel.y*self.dir.y
    
    def display(self):
        fill("#ffff64")
        noStroke()
        ellipse(self.pos.x, self.pos.y, self.r*2, self.r*2)
    
    def checkEdges(self):
        # rechter Rand
        if (self.pos.x > width - self.r and self.dir.x > 0):
            self.dir.x *= -1
        # linker Rand
        if (self.pos.x < self.r and self.dir.x < 0):
            self.dir.x *= -1
        # top
        if (self.pos.y < self.r and self.dir.y < 0):
            self.dir.y *= -1
        # bottom (wird später gelöscht)
        if (self.pos.y > height - self.r and self.dir.y > 0):
            self.dir.y *= -1
~~~

Der *Ball* bekommt im Konstuktor einen Radius, eine Velocity und eine Richtung verpaßt. Diese werden jeweils als `PVector` implementiert. Ebenfalls ein `PVector` ist die Position, mit der der Ball erst einmal in die Mitte des Fenster plaziert wird. Wie aber die `update()`-Methode zeigt, bewegt sich der Ball sofort und zwar erst einmal nach rechts unten. Sobald der Ball jedoch eine der Kanten des Fensters erreicht, *bounced* ihn `checkEdges()` zurück. Die Methode `update()` zeigt einfach nur den Ball in einer tennisballgelben Farbe an.

Das Hauptprogramm sieht jetzt erst einmal so aus:

~~~python
from gameworld import Paddle, Ball

def setup():
    global paddle, ball
    size(605, 400)
    paddle = Paddle()
    ball = Ball()

def draw():
    global paddle, ball
    background(0, 0, 0)
    paddle.display()
    paddle.checkEdges()
    paddle.update()
    ball.display()
    ball.checkEdges()
    ball.update()
    
def keyReleased():
    global paddle
    paddle.isMovingRight = False
    paddle.isMovingLeft = False

def keyPressed():
    global paddle
    if key == CODED:
        if keyCode == LEFT:
            paddle.isMovingLeft = True
        elif keyCode == RIGHT:
            paddle.isMovingRight = True
~~~

Der Ball *bounced* hin und her und ignoriert das *Paddle* geflissentlich. Vorerst bleibt das so, denn als nächstes möchte ich erst einmal die *Bricks* implementieren.

## Das Spiel starten

Bevor ich aber die Steine implementiere, möchte ich erst einmal den ärgerlichen Umstand beheben, daß das Spiel erst dann auf die Tasteneingaben reagiert, wenn man mit der Maus in das Spielfenster klickt und diesem den Focus gibt. Also startet das Spiel auch erst, wenn man mit der Maustaste in das Fenster klickt, vorher passiert gar nichts. Dafür habe ich an den Anfang des Sketches mit

~~~python
playingGame = False
~~~

eine boolsche Variable initialisiert und weiter unten die Funktion

~~~python
def mousePressed():
    global playingGame
    playingGame = True
~~~

hinzugefügt. Die `draw()`-Schleife wurde ebenfalls entsprechend geändert:

~~~python
    # Paddle
    paddle.display()
    if playingGame:
        paddle.checkEdges()
        paddle.update()
    # Ball
    if (ball.meets(paddle)):
        if (ball.dir.y > 0):
            ball.dir.y *= -1
    ball.display()
    if playingGame:
        ball.checkEdges()
        ball.update()
~~~

Eigentlich ist damit alles erledigt, nur leider ist das Spiel nun für Rechtshänder unspielbar geworden. Denn bevor man mit der rechten Hand von der Maus an die Pfeiltasten gekommen ist, ist der Ball schon lange im Aus. Daher habe ich eine alte Spieltechnik zusätzlich implementiert, Neben den Pfeiltasten steht `a` für die Bewegung des *Paddles* nach links und `d` für die Bewegung nach rechts. Dazu mußte die Funktion `keyPressed()` geändert werden:

~~~python
def keyPressed():
    global paddle
    if key == "a" or key == "A":
        paddle.isMovingLeft = True
    elif key == "d" or key == "D":
        paddle.isMovingRight = True
    if key == CODED:
        if keyCode == LEFT:
            paddle.isMovingLeft = True
        elif keyCode == RIGHT:
            paddle.isMovingRight = True
~~~

Nun kann man beim Start mit der rechten Hand die Maustaste drücken und mit der linken Hand schon über dem `d` lauern, damit man sofort, wenn sich der Ball in Bewegung setzt, auch das *Paddle* nach rechts bewegen kann. Irgendwann im Verlauf des Spiels werden Rechtshänder vermutlich wieder zu den Pfeiltasten wechseln, aber Linkshänder sind mit der `a`-`d`-Kombination vielleicht generell glücklicher.

Nun soll natürlich der Ball, wenn er mit dem *Paddle* kollidiert, auch auf diesen reagieren. Dazu erhält er in der Klasse `Ball` noch die Methode `meets()`, die im obigen Code-Schnipsel auch schon aufgerufen wird:

~~~python
    def meets(self, paddle):
        if (self.pos.y < paddle.pos.y and
            self.pos.y > paddle.pos.y - self.r and
            self.pos.x > paddle.pos.x - self.r and
            self.pos.x < paddle.pos.x + paddle.w + self.r):
            return True
        else:
            return False
~~~

Es ist eine boolsche Methode, die `True` zurückliefert, wenn der Ball auf das *Paddle* trifft und andernfals `False`. Und in der Hauptschleife kann man dann mit

~~~python
    if (ball.meets(paddle)):
        if (ball.dir.y > 0):
            ball.dir.y *= -1
~~~

einfach die y-Richtung umkehren, wenn `meets()` `True` zurückliefert. Zu Übungszwecken und um die Implementierung zu testen, bounced der Ball zu diesem Zeitpunkt immer noch auch vom Boden des Fensters zurück, dieses Verhalten möchte ich erst ganz zum Schluß ändern.

## Jetzt aber: Die Klötzchen

Ich möchte drei Reihen von Klötzchen implementieren, die verschiedene »Leben« haben. Die unterste Reihe (grün) hat nur ein Leben und das Klötzchen verschwindet sofort, wenn es vom Ball getroffen wird. Die mittlere Reihe (rosa) hat zwei Leben, beim ersten Treffen des Balls verfärbt sich das Klötzchen grün und Anzahl der Leben wird um eines herabgesetzt. Analog hat die oberste Reihe (lila) drei Leben. Wird dort ein Klötzchen zum ersten Mal getroffen, wird es rosa, hat nur noch zwei Leben und wenn es dann noch einmal getroffen wird, wird es grün und besitzt nur noch ein Leben. Die Implementierung der Klasse `Brick` beginnt daher so:

~~~python
class Brick(object):
    
    COLORS = {1: "#64ff96", 2: "#ff6496", 3: "#9664ff"}
    
    def __init__(self, x, y, hits):
        self.w = 75
        self.h = 20
        self.pos = PVector(x, y)
        self.hits = hits
        self.col = Brick.COLORS[hits]
    
    def display(self):
        fill(self.col)
        stroke("#ffffff")
        strokeWeight(2)
        rect(self.pos.x, self.pos.y, self.w, self.h)
~~~

Der Konstruktor übernimmt drei Parameter, die x- und y-Position sowie die Anzahl der Hits. Die Methode `display()` stellt jedes Klötzchen in seiner Farbe und an seiner Position dar. Der weiße, zwei Pixel starke Rand soll die einzelnen Klötzchen während der Entwicklung deutlich unterscheidbar machen.

Das Hauptprogramm bekommt nun folgende Ergänzungen. Ganz oben wird mit

~~~python
from gameworld import Paddle, Ball, Brick

bricks = []
~~~

eine leere Liste `bricks` initialisiert, die dann in `setup()` gefüllt wird:

~~~python
    for x in range(5, width - 80, 75):
        addBrick(x + 37.5, 50, 3)
        addBrick(x + 37.5, 70, 2)
        addBrick(x + 37.5, 90, 1)
~~~

dazu muß dem Programm auch noch die Funktion `addBrick(x, y, hits)` hinzugefügt werden:

~~~python
def addBrick(x, y, hits):
    global brick, bricks
    brick = Brick(x, y, hits)
    bricks.append(brick)
~~~

Und die Darstellung in der `draw()`-Schleife sieht dann so aus:

~~~python
def draw():
    global paddle, ball, bricks, playingGame
    background(0, 0, 0)
    # Bricks
    for i in range(len(bricks)):
        bricks[i].display()
~~~

Nun gewinnt man schon einen ungefähren Eindruck, wie das Spiel einmal aussehen soll. Man kann den Ball mit dem Paddle auffangen -- mit ein wenig Geschick auch zu Beginn des Spieles, aber ansonsten bewegt der tennisgelbe Ball sich weiterhin wie ein *Bouncing Ball*. Als nächstes werden ich daher die Kollision mit den Klötzchen implementieren.
