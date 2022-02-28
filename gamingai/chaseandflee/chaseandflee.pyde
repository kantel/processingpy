WIDTH, HEIGHT = 640, 480
dia           = 30
chaserSpeed   = 2.0
fleeSpeed     = -2.0

player = PVector(0, 0)
chaser = PVector(WIDTH/2, HEIGHT/2)
flee   = PVector(WIDTH/2, 3*HEIGHT/4)

def setup():
    size(WIDTH, HEIGHT)
    this.windowTitle("Flucht und Verfolgung (ohne OOP)")
    cursor(CROSS)
    
def draw():
    background(248, 158, 80)
    
    # Player Update
    player.x = mouseX
    player.y = mouseY
    
    # Chaser Update
    dir = PVector.sub(player, chaser)
    dir.normalize().mult(chaserSpeed)
    chaser.add(dir)
    
    # Flee Update
    distBetween = player.dist(flee)
    if distBetween < 100:
        dir = PVector.sub(player, flee)
        dir.normalize().mult(fleeSpeed)
        flee.add(dir)
    # Emergency Exit
    if flee.x > width - dia/2 or flee.x < dia/2:
        flee.x = width/2
    if flee.y > height - dia/2 or flee.y < dia/2:
        flee.y = 3*height/4

    stroke(0)
    strokeWeight(1)
    # Player Show
    fill(240, 80, 37)
    circle(player.x, player.y, dia)
    
    # Chaser Show
    fill(98, 199, 119)
    circle(chaser.x, chaser.y, dia)
    
    # Flee Show
    fill(240, 99, 164)
    circle(flee.x, flee.y, dia)
    
def keyPressed():
    noLoop()
