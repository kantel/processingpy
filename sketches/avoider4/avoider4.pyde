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
    for i in range(len(smiley)):
        if skull.checkCollision(smiley[i]):
            if skull.health > 0:
                skull.health -= 1
                smiley[i].reset(randint(0, w-tw), -randint(50, 250))
            else:
                playgame = False
                gameover = True 
    skull.display()
    for i in range(len(smiley)):
        smiley[i].move()
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
        