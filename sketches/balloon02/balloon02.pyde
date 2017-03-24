from balloon import Balloon
numBalloons = 10
balloons = []

def setup():
    global jahrmarkt
    size(640, 320)
    balloonPic = loadImage("1f388.png")
    jahrmarkt = loadImage("jahrmarkt.jpg")
    i = 0
    while (i < numBalloons):
        dia = random(36, 72)
        balloons.append(Balloon(dia, balloonPic))
        i += 1

def draw():
    global jahrmarkt
    background(jahrmarkt)
    for i in range(len(balloons)):
        balloons[i].move()
        balloons[i].display()
        balloons[i].top()
