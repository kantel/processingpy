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
    
    strokeWeight(baseStroke)
    noFill()
    # Sekunden
    stroke(150, 100, 255)
    arc(0, 0, 300, 300, radians(0), radians(secondAngle))
    # Minuten
    stroke(255, 100, 150)
    arc(0, 0, 320, 320, radians(0), radians(minuteAngle))
    # Stunden
    stroke(150, 255, 100)
    arc(0, 0, 340, 340, radians(0), radians(hourAngle))


    
    
    
    
    