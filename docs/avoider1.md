# Avoider Game Stage 1

Zum Abschluß meiner kleinen, geplanten Tutorial-Reihe zu Processing.py, dem Python-Mode von Processing, möchte ich mit und für Euch ein kleines, vollständiges Spieleprojekt programmieren. Es basiert zum einen auf dem »[AS3 Avoider Game Tutorial](http://gamedev.michaeljameswilliams.com/as3-avoider-game-tutorial-base/)«, das *Michael James Williams* für ActionScript 3 und Flash geschrieben hat und das *Michael Haungs* dann in seinem Buch »[Creative Greenfoot][a1]« nach Java und Greenfoot portierte. Zum anderen habe ich es noch mit Ideen aus einem Programm aus dem wundervollen Buch »[Game Programming][a2]«, einem PyGame-Tutorial von *Andy Harris* aufgepeppt, in dem ein Postflieger Inseln anfliegen, aber Wolken vermeiden muß.

## Die Spiel-Idee

[![Screenshot](images/avoider1.jpg)](https://www.flickr.com/photos/schockwellenreiter/36501204602/)

Ziel des Spiels ist es, daß der Held seinen von oben herabregnenden Feinden ausweichen muß. Doch in diesem Spiel ist nichts so, wie es scheint: Die Feinde sind lächelnde Smileys und unser Held ist ein häßlicher Totenkopfschädel. Im ersten Stadium möchte ich nur dieses einfache Spieleprinzip und einen *Highscore* implementieren, in den nächsten Tutorials möchte ich dieses mit weiteren Variationen und Ideen zu einem interessanteren Spiel ausbauen.

## Das Sprite-Modul

Wie schon mehrmals praktiziert, lege ich erst einmal einen separaten Tab `spite.py` an, der in der Hauptsache die Klasse `Sprite` und die davon abgeleiteten Unterklassen `Skull` und `Smiley` beherbergt:

~~~python
from random import randint

tw = th = 36

class Sprite():
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.over = False

    def checkCollision(self, otherSprite):
        if (self.x < otherSprite.x + tw and otherSprite.x < self.x + tw
            and self.y < otherSprite.y + th and otherSprite.y < self.y + th):
            return True
        else:
            return False

class Skull(Sprite):
    
    def loadPics(self):
        self.im1 = loadImage("skull.png")
        
    def move(self):
        self.x = mouseX
        if self.x <= 0:
            self.x = 0
        elif self.x >= width-tw:
            self.x = width - tw
            
    def display(self):
        image(self.im1, self.x, self.y)

class Smiley(Sprite):
    
    def loadPics(self):
        self.im0 = loadImage("smiley0.png")
        self.im1 = loadImage("smiley1.png")
        self.im2 = loadImage("smiley4.png")
        
    def move(self):
        self.over = False
        self.y += self.dy
        if self.y >= height:
            self.over = True
            self.y = -randint(50, 250)
            self.x = randint(0, width-tw)
            self.dy = randint(2, 10)
        
    def display(self):
        if (self.y > -30) and (self.y <= 200):
            image(self.im0, self.x, self.y)
        elif (self.y > 200) and (self.y <= 360):
            image(self.im1, self.x, self.y)
        elif (self.y > 360):
            image(self.im2, self.x, self.y)
~~~

Für die Bilder der Akteure habe habe ich mich wieder bei den freien [Twitter Emojis](https://github.com/twitter/twemoji) bedient und hier sind sie, damit Ihr das Spiel nachprogrammieren könnt:

![skull](images/skull.png) ![smiley0](images/smiley0.png) ![smiley1](images/smiley1.png) ![smiley4](images/smiley4.png)

Die Bilder sind jeweils 36x36 Pixel groß, das habe ich in den Variablen `tw` und `th` festgehalten. Unser armer Held, der den grinsenden Smileys ausweichen muß, soll mit der Maus gesteuert werden. Dabei kann er sich nur horizontal bewegen, sein vertikaler Standort ist im Programm festverdrahtet. Mit den Zeilen

~~~python
        if self.x <= 0:
            self.x = 0
        elif self.x >= width-tw:
            self.x = width - tw
~~~

ist sichergestellt, daß er das Spielfeld nicht heimlich verlassen kann, um sich den Grinsebacken zu entziehen. Diese grinsen tatsächlich nicht immer: Fröhlich stürzen sie herab, strecken auf der Höhe unseres Helden die Zunge heraus, um dann, wenn sie merken, daß sie ihn nicht getroffen haben, mit verärgertem Gesicht in die Tiefe zu stürzen. Dazu wird ihnen je nach Y-Koordinate in der `display()`-Funktion das entsprechende Bildchen zugewiesen:

~~~python
    def display(self):
        if (self.y > -30) and (self.y <= 200):
            image(self.im0, self.x, self.y)
        elif (self.y > 200) and (self.y <= 360):
            image(self.im1, self.x, self.y)
        elif (self.y > 360):
            image(self.im2, self.x, self.y)
~~~

Die Smileys stürzen natürlich nicht ins Bodenlose. Ich wollte mir den Streß ersparen und die Smiley-Objekte löschen zu müssen, nachdem sie das Spielfeld verlassen haben. Stattdessen habe ich im Hauptprogramm die Anzahl der Smileys konstant gesetzt (es sind zehn) und diese jedesmal, wenn sie das Spielefenster verlassen haben, habe ich sie an einer zufälligen Position weit oberhalb des Fensters wieder neu positioniert:

~~~python
            self.y = -randint(50, 250)
            self.x = randint(0, width-tw)
            self.dy = randint(2, 10)
~~~

Mit der letzten Zeile wird ihnen dabei auch noch zufällig eine neue Geschwindigkeit zugewiesen, so daß der Spieler nicht merkt, daß er es immer wieder mit den gleichen Akteuren zu tun hat.

## Das Hauptprogramm

Nun zum Hauptprogramm. Es ist zwar nicht ganz so kurz geraten, wie einige andere, die ich hier schon vorgestellt hatte, aber eigentlich immer noch übersichtlich:

~~~python
from random import randint
from sprite import Skull, Smiley

w = 640
tw = th = 36
noSmileys = 10
startGame = True
playGame = False
gameOver = False


skull = Skull(w/2, 320)
smiley = []
for i in range(noSmileys):
    smiley.append(Smiley(randint(0, w-tw), randint(50, 250)))

def setup():
    skull.score = 0
    size(640, 480)
    frameRate(30)
    skull.loadPics()
    for i in range(len(smiley)):
        smiley[i].loadPics()
        smiley[i].dy = randint(2, 10)
    font = loadFont("ComicSansMS-32.vlw")
    textFont(font, 32)
  
def draw():
    global startGame, playGame, gameOver
    background(0, 0, 0)
    text("Score: " + str(skull.score), 10, 32)
    if startGame:
        text("Klick to Play", 200, height/2)
        if mousePressed:
            startGame = False
            playGame = True
    elif playGame:
        skull.move()
        for i in range(len(smiley)):
            if skull.checkCollision(smiley[i]):
                playGame = False
                gameOver = True        
        skull.display()
        for i in range(len(smiley)):
            smiley[i].move()
            if smiley[i].over:
                skull.score += 1
            smiley[i].display()
    elif gameOver:
        text("Game Over!", 200, height/2)
~~~

Für dieses Spiel habe ich mir mal erlaubt, die allgemein verpönte Schrift `Comic Sans` zu verwenden, denn nichts ist hier so, wie es scheint: Das Böse ist gut und das Gute ist böse. Die Entsprechende `.vlw`-Datei habe ich mit dem Tool »Schrift erstellen« (in `Tools -> Schrift erstellen …`) erzeugt und wie die Bildchen in den `data`-Folder des Sketches abgelegt.

Nach dem Import der Klassen `Skull` und `Smiley` habe ich die entsprechenden Objekte erzeugt und ihnen ihre Startposition zugewiesen. Im `setup()` werden dann die Bilder geladen und den Smileys je eine eigene, zufällige Geschwindigkeit (`dy`) zugewiesen.

Etwas komplizierter ist die `draw()`-Funktion aufgebaut. Wegen der Eigenheit von Processing.py, daß das Programm zwar aus der IDE heraus startet, das Programmfenster aber dann noch nicht den Fokus besitzt (den hat nach wie vor die IDE), war es notwendig, einen Startbildschirm vorzuschalten, der das Spiel erst nach einem Mausklick startet (und damit dem Programmfenster auch den Fokus gibt). Und natürlich sollte es auch einen »Game Over«-Bildschirm geben. Daher habe ich drei globale Zustandvariablen (`startGame`, `playGame` und `gameOver`) definiert und je nach ihrem Zustand werden dann die jeweiligen Bildschirme angezeigt.

Jeder Smiley, der das Fenster verläßt, ohne mit dem Schädel zu kollidieren, erhöht den Score des Spielers um einen Punkt. Dazu wurde die Variable `over` schon in der Klasse Smiley erzeugt, die jedesmal, wenn ein Smiley das Fenster verläßt

~~~python
        if self.y >= height:
            self.over = True
~~~

auf `True` gesetzt wird. Dies wird aber beim nächsten Druchlauf in

~~~python
    def move(self):
        self.over = False
~~~

sofort wieder zurückgesetzt. Im Hauptprogramm wird dann in den Zeilen

~~~python
            if smiley[i].over:
                skull.score += 1
~~~

der Zustand abgefragt und der Score entsprechend hochgesetzt.

Das Programm ist tatsächlich spielbar. Passt der Spieler nicht auf und kollidiert mit einem der Smileys, dann ist es unbarmherzig zu Ende und es heißt »Game Over!«


[a1]: https://www.amazon.de/Creative-Greenfoot-Michael-Haungs/dp/1783980389/ref=as_li_ss_tl?ie=UTF8&qid=1503160042&sr=8-1&keywords=Creative+Greenfoot&linkCode=ll1&tag=derschockwell-21&linkId=e9b13f6f5e11c34b606d9e8d6bffcb10
[a2]: https://www.amazon.de/Game-Programming-Express-Line-Learning/dp/0470068221/ref=as_li_ss_tl?&linkCode=ll1&tag=derschockwell-21&linkId=e73cc33dbae2dbe0f72dbbe560f3b008