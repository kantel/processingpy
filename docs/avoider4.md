# Avoider Game Stage 4: PowerUp und PowerDown

Im vierten und letzten Teil meiner kleinen Serie über die Programmierung des Avoider-Spiels in Processing.py wollte ich das Spiel noch mit ein paar zusätzlichen Akteuren aufpeppen. Dazu habe ich *Power Items* eingeführt, die entweder dem Spieler zusätzliche Leben geben oder nehmen, also je ein *PowerUp* und ein *PowerDown*. Als besonderes Highlight bewegen diese sich auf anderen Wegen durch das Spielefenster als die Smileys und sind daher etwas unberechenbarer für den Spieler. Gemäß dem Motto des Spieles, daß man niemanden trauen darf, das gut aussieht, ist das PowerUp, das dem Spieler ein weiteres Leben schenkt, ein grimmig aussehendes Gespenst und das PowerDown, das ihm ein Leben nimmt, ein lecker aussehendes Tassentörtchen.

![Ghost](images/ghost.png) ![Cupcake](images/cupcake.png)

Auch diese Bilder habe ich wieder den freien [Twitter Emojis](https://github.com/twitter/twemoji) *(Twemojis)* entnommen und hier sind sie, damit Ihr das Spiel nachprogrammieren könnt.

## Power Items

Als erstes habe ich im Reiter `sprite.py` eine Klasse `PowerItem` angelegt, die von `Sprite` erbt:

~~~python
class PowerItem(Sprite):
    
    def __init__(self, posX, posY, tX, tY, eT):
        super(PowerItem, self).__init__(posX, posY)
        self.origX = posX
        self.origY = posY
        self.targetX = tX
        self.targetY = tY
        self.expireTime = eT
        self.duration = self.expireTime/2.0
        self.counter = 0
        self.pause = randint(10, 150)
        
    def curveX(self, x):
        return x
    
    def curveY(self, y):
        return y
    
    def easing(self):
        self.counter += 1
        self.fX = self.fY = (self.counter)/float(self.duration)
        self.fX = self.curveX(self.fX)
        self.fY = self.curveY(self.fY)
        self.x = (self.targetX * self.fX) + (self.origX * (1.0 - self.fX))
        self.y = (self.targetY * self.fY) + (self.origY * (1.0 - self.fY))

    def move(self):
        self.expireTime -= 1
        if self.expireTime < 0:
            self.pause -= 1
            if self.pause < 0:
                self.reset()
    
    def display(self):
        # print(self.x, self.y)
        image(self.im1, self.x, self.y)
    
    def reset(self):
        self.origX = randint(-150, width-tw)
        self.origY = -randint(50, 250)
        self.targetX = randint(tw, width-tw)
        self.targetY = randint(tw, height-tw)
        self.expireTime = self.duration*2.0
        self.counter = 0
        self.pause = randint(10, 150)
~~~

Die *Power Items* haben nur eine gewisse Lebensdauer und bewegen sich während ihrer Lebenszeit (`eT`) von der Startposition (`posX`, `posY`) zur Zielposition (`tX`, `tY`). Diese Parameter müssen daher dem Konstruktor übergeben werden.

Wie alle Akteure prasseln die *Power Items* zu Beginn des Spieles quasi gleichzeitig vom oberen Fensterrand auf den Spieler nieder, damit sich die Lage in den folgenden Runden entspannt, habe ich den einzelnen Items nach Ende ihren Lebens eine Pause verordnet, deren Länge vom Zufallszahlengenerator bestimmt wird, bevor sie wieder die Arena betreten dürfen.

## Easing

Das Prinzip des *[Easings](https://processing.org/examples/easing.html)* hatte ich [in diesem Beispiel](rauhnaechte.md) schon einmal eingeführt. Es war ein einfaches, lineares Easing, in dem die Figur immer langsamer wurde, je mehr sie sich dem Ziel näherte. Dieses lineare Easing ist auch in der Klasse `PowerItem` implementiert, aber so, daß es verändert werden kann, wenn die abgeleiteten Klassen die Methoden `curveX()` und/oder `curveY()` überschreiben. Außerdem wird die Geschwindigkeit und neue Position unter anderem auch von der Lebensdauer des *Power Items* beeinflußt.

In den von `PowerItem` abgeleiteten Klassen `Ghost` und `Cupcake` mußten also nur die entsprechenden Bildchen geladen und die Methode `curveY()` überschreiben:

~~~python
class Ghost(PowerItem):
    
    def loadPics(self):
        self.im1 = loadImage("ghost.png")
    
    
    def curveY(self, y):
        return y**5

class Cupcake(PowerItem):
    
    def loadPics(self):
        self.im1 = loadImage("cupcake.png")
    
    def curveY(self, y):
        return 3*sin(3*y)
~~~

Im Falle des *Power Up*, des Gespenstes, bewegt sich das *Power Item* in einer expotentionellen Kurve von oben nach unten und wird immer schneller, je tiefer es fällt. Der Spieler muß sich schon beeilen, um mit diesem Item zu kollidieren, um ein zusätzlichres Leben einzufangen. Dagegen habe ich mir im Falle des Tassentörtchens etwas Gemeines überlegt: Die einzelnen Törtchen bewegen sich auf einer übergroßen Sinuskurve durch das Geschehen. Daher kann es durchaus passieren, daß die Törtchen, nachdem sie das Fenster am unteren Rand verlassen haben, von dort auch wieder auftauchen und nach oben schießen. Das macht es dem Spieler schwieriger, ihnen auszuweichen. Also: Die Kollision mit den *Power Ups* ist schwierig, umgekehrt it es schwer, den *Power Downs* auszuweichen. Schießlich soll es dem Spieler ja nicht zu einfach vorkommen.

Die jeweiligen Werte in der Methode `curveY()` habe ich durch wildes Experimentieren herausgefunden.

## Das Hauptprogramm

![Screenshot](images/screenshot-1099.png)

Im Hauptprogramm sind die wichtigsten Änderungen in der Funktion `playGame()` vorgenommen worden, die folgende zusätzliche Zeilen erhielt:

~~~python
    for i in range(len(ghost)):
        ghost[i].easing()
        ghost[i].move()
        if ghost[i].checkCollision(skull):
            if skull.health < 5:
                skull.health += 1
                ghost[i].reset()
        ghost[i].display()
    for i in range(len(cupcake)):
        cupcake[i].easing()
        cupcake[i].move()
        if cupcake[i].checkCollision(skull):
            skull.health -= 1
            cupcake[i].reset()
        cupcake[i].display()
~~~

Für jedes *Power Item* wird erst das *Easing* berechnet, dann die neue Position bestimmt, überprüft ob es mit dem Spieler kollidiert und dann wird es angezeigt. Außerdem lasse ich als kleine Optimierung nicht mehr in jedem Frame den Spieler prüfen, ob er mit einem der Smileys kollidiert (das muß er nämlich jedes Mal mit *allen* Smileys machen), sondern nun überprüfen -- wie bei den *Power Items* -- die Smileys, ob sie mit dem Spieler kollidieren:

~~~python
    for i in range(len(smiley)):
        smiley[i].move()
        if smiley[i].checkCollision(skull):
            skull.health -= 1
            smiley[i].reset(randint(0, w-tw), -randint(50, 250))
        if smiley[i].outside:
            skull.score += 1
        smiley[i].display()
~~~

Das Spiel startet in meiner Version mit zehn Smileys, drei Gespenstern und fünf Tassentörtchen. Das sind 18 Akteure auf die der Spieler aufpassen muß und das macht das Spiel schon ganz schön schwierig, aber ohne daß es unfair wirkt oder gar unspielbar ist.

## Der Quellcode

Und nun -- wie immer -- der vollständige Quellcode, damit Ihr das Spiel nachprogrammieren und nachvollziehen könnt. Als erstes wieder der Code aus dem Reiter `sprite.py`:

~~~python
from random import randint

tw = th = 36

class Sprite(object):
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY

    def checkCollision(self, otherSprite):
        if (self.x < otherSprite.x + tw and otherSprite.x < self.x + tw
            and self.y < otherSprite.y + th and otherSprite.y < self.y + th):
            return True
        else:
            return False


class Skull(Sprite):

    def __init__(self, posX, posY):
        super(Skull, self).__init__(posX, posY)
        self.score = 0
        self.health = 0
            
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
    
    def __init__(self, posX, posY):
        super(Smiley, self).__init__(posX, posY)
        self.outside = False

    def loadPics(self):
        self.im0 = loadImage("smiley0.png")
        self.im1 = loadImage("smiley1.png")
        self.im2 = loadImage("smiley4.png")
        
    def move(self):
        self.outside = False
        self.y += self.dy
        if self.y >= height:
            self.outside = True
            self.y = -randint(50, 250)
            self.x = randint(0, width-tw)
            self.dy = randint(4, 10)
        
    def display(self):
        if (self.y > -30) and (self.y <= 250):
            image(self.im0, self.x, self.y)
        elif (self.y > 250) and (self.y <= 320):
            image(self.im1, self.x, self.y)
        elif (self.y > 320):
            image(self.im2, self.x, self.y)
    
    def reset(self, posX, posY):
        self.x = posX
        self.y = posY

class PowerItem(Sprite):
    
    def __init__(self, posX, posY, tX, tY, eT):
        super(PowerItem, self).__init__(posX, posY)
        self.origX = posX
        self.origY = posY
        self.targetX = tX
        self.targetY = tY
        self.expireTime = eT
        self.duration = self.expireTime/2.0
        self.counter = 0
        self.pause = randint(10, 150)
        
    def curveX(self, x):
        return x
    
    def curveY(self, y):
        return y
    
    def easing(self):
        self.counter += 1
        self.fX = self.fY = (self.counter)/float(self.duration)
        self.fX = self.curveX(self.fX)
        self.fY = self.curveY(self.fY)
        self.x = (self.targetX * self.fX) + (self.origX * (1.0 - self.fX))
        self.y = (self.targetY * self.fY) + (self.origY * (1.0 - self.fY))

    def move(self):
        self.expireTime -= 1
        if self.expireTime < 0:
            self.pause -= 1
            if self.pause < 0:
                self.reset()
    
    def display(self):
        # print(self.x, self.y)
        image(self.im1, self.x, self.y)
    
    def reset(self):
        self.origX = randint(-150, width-tw)
        self.origY = -randint(50, 250)
        self.targetX = randint(tw, width-tw)
        self.targetY = randint(tw, height-tw)
        self.expireTime = self.duration*2.0
        self.counter = 0
        self.pause = randint(10, 150)
        
class Ghost(PowerItem):
    
    def loadPics(self):
        self.im1 = loadImage("ghost.png")
    
    
    def curveY(self, y):
        return y**5

class Cupcake(PowerItem):
    
    def loadPics(self):
        self.im1 = loadImage("cupcake.png")
    
    def curveY(self, y):
        return 3*sin(3*y)
    
            
class Star(object):
    
    def __init__(self, posX, posY, dia, speed):
        self.x = posX
        self.y = posY
        self.r = dia
        self.dy = speed
        self.a = 255 # Transparency
    
    def move(self):
        self.outside = False
        self.y += self.dy
        if self.y >= height:
            self.outside = True
            self.y = -2*self.r
            self.x = randint(0, width - 2*self.r)
    
    def display(self):
        fill(255, 255, 255, self.a)
        noStroke()
        ellipse(self.x, self.y, self.r, self.r)
~~~

Und dann das eigentliche Hauptprogramm, das ebenfalls noch einmal an Umfang zugenommen hat:

~~~python
from random import randint
from sprite import Skull, Smiley, Ghost, Cupcake, Star

w = 640
h = 480
tw = th = 36
noSmileys = 10
nobStars = 30
nonStars = 15
noGhost = 3
noCupcakes = 5
startgame = True
playgame = False
gameover = False

skull = Skull(w/2, 320)
smiley = []
bStar = []
nStar = []
ghost = []
cupcake = []

def setup():
    global heart
    size(640, 480)
    frameRate(30)
    loadData()
    skull.score = 0
    skull.health = 5
    skull.loadPics()
    for i in range(len(smiley)):
        smiley[i].loadPics()
        smiley[i].dy = randint(4, 10)
    for i in range(len(ghost)):
        ghost[i].loadPics()
    for i in range(len(cupcake)):
        cupcake[i].loadPics()
    font = loadFont("ComicSansMS-32.vlw")
    textFont(font, 32)
    heart = loadImage("heart.png")
    # noCursor()
    # cursor(HAND)
  
def draw():
    global heart
    background(0, 0, 0)
    fill(255, 255, 255, 255)
    text("Score: " + str(skull.score), 10, 32)
    for i in range(skull.health):
        image(heart, width - i*tw - tw - 2, 2)
    if startgame:
        startGame()
    elif playgame:
        playGame()
    elif gameover:
        gameOver()

def loadData():
    for i in range(noSmileys):
        smiley.append(Smiley(randint(0, width-tw), -randint(50, 250)))
    for i in range(noGhost):
        ghost.append(Ghost(randint(-150, width-tw), -randint(50, 250), randint(tw, width-tw), randint(tw, height-tw), 300))
    for i in range(noCupcakes):
        cupcake.append(Cupcake(randint(-150, width-tw), -randint(50, 250), randint(tw, width-tw), randint(tw, height-tw), 600))
    for i in range(nobStars):
        bStar.append(Star(randint(0, width-2), randint(2, height-2), 1, 0.1))
    for i in range(nonStars):
        nStar.append(Star(randint(0, width-4), randint(2, height-2), randint(2, 3), 0.2))

def startGame():
    global startgame, playgame
    text("Klick to Play", 200, height/2)
    if mousePressed:
        startgame = False
        playgame = True
        
def playGame():
    global playgame, gameover
    for i in range(len(bStar)):
        bStar[i].move()
        bStar[i].display()
    for i in range(len(nStar)):
        nStar[i].move()
        if (frameCount % randint(15, 30)) < randint(1, 15):
            nStar[i].a = 120
        else:
            nStar[i].a = 255
        nStar[i].display()
    skull.move()
    if skull.health < 0:
        playgame = False
        gameover = True 
    skull.display()
    for i in range(len(smiley)):
        smiley[i].move()
        if smiley[i].checkCollision(skull):
            skull.health -= 1
            smiley[i].reset(randint(0, w-tw), -randint(50, 250))
        if smiley[i].outside:
            skull.score += 1
        smiley[i].display()
    for i in range(len(ghost)):
        ghost[i].easing()
        ghost[i].move()
        if ghost[i].checkCollision(skull):
            if skull.health < 5:
                skull.health += 1
                ghost[i].reset()
        ghost[i].display()
    for i in range(len(cupcake)):
        cupcake[i].easing()
        cupcake[i].move()
        if cupcake[i].checkCollision(skull):
            skull.health -= 1
            cupcake[i].reset()
        cupcake[i].display()

def gameOver():
    global playgame, gameover
    text("Game Over!", 200, height/2)
    text("Klick to play again.", 200, 300)
    if mousePressed:
        gameover = False
        for i in range(len(smiley)):
            smiley[i].reset(randint(0, w-tw), -randint(50, 250))
        for i in range(len(ghost)):
            ghost[i].reset()
        for i in range(len(cupcake)):
            cupcake[i].reset()
        playgame = True
        skull.health = 5
        skull.score = 0
        
def mousePressed():
    global playgame
    if playgame:
        saveFrame("frames/screenshot-####.png")
~~~

## Screenshots

Bei diesem Spiel ist es nahezu unmöglich, mit den Bordmitteln des Betriebssystems noch aussagefähige Screenshots wie den oben im Beitrag zu erstellen. Daher habe ich das mit Processing-eigenen Mitteln erledigt: Die Funktion `mousePressed()`

~~~python
def mousePressed():
    global playgame
    if playgame:
        saveFrame("frames/screenshot-####.png")
~~~

schießt jedes Mal, wenn die linke Maustaste gedrückt wird, einen aktuellen Screenshot. Aus dem fertigen Spiel solltet Ihr diese Funktion natürlich wieder herausnehmen.

Das war es mit dem *Avoider Game*. Natürlich sind noch jede Menge Erweiterungen möglich und auch die Gestaltung des Start- und des Game-Over-Bildschirms kann sicher noch verschönert werden. Mir kam es aber darauf an, zu zeigen, wie in Processing.py mit einfachen Mitteln doch schnell ein ansprechendes Spiel programmiert werden kann. Alles weitere ist Eurer Phantasie überlassen.