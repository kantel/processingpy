easing1 = 0.01
easing2 = 0.05
ghostX = 240
ghostY = 200
engelX = 200
engelY = 240

def setup():
    global bg, ghost, engel
    bg = loadImage("koken.jpg")
    ghost = loadImage("ghost.png")
    engel = loadImage("engel.png")
    frameRate(30)
    size(560, 320)
  
def draw():
    global ghostX, ghostY, engelX, engelY
    background(bg)
    targetX = mouseX
    targetY = mouseY
    
    engelX += (targetX - engelX) * easing1
    if engelX >= (width - 36):
        engelX = width - 36
    elif engelX <= 0:
        engelX = 0;
    engelY += (targetY - engelY) * easing1
    if engelY >= (height - 36):
        engelY = height - 36
    elif engelY <= 0:
        engelY = 0
    image(engel, engelX, engelY)
    
    ghostX += (targetX - ghostX) * easing2
    if ghostX >= (width - 36):
        ghostX = width - 36
    elif ghostX <= 0:
        ghostX = 0;
    ghostY += (targetY - ghostY) * easing2
    if ghostY >= (height - 36):
        ghostY = height - 36
    elif ghostY <= 0:
        ghostY = 0
    image(ghost, ghostX, ghostY)

    
    