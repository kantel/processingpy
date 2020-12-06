from hero import Hero

yoffset = 80
tilesize = 32

def setup():
    global hero_images, ground01, player
    size(512, 512)
    ground01 = loadImage("ground01.png")
    player = Hero(8, 4)

def draw():
    background(0, 0, 0)    
    image(ground01, 0, yoffset)

    strokeWeight(1)
    stroke(255, 255, 255)
    for y in range(11):
        line(0, (tilesize*y) + yoffset, width, (tilesize*y) + yoffset)
        for x in range(16):
            line(tilesize*x, yoffset, tilesize*x, height - yoffset)
    player.update()
    player.show()
        

def keyPressed():
    if key == CODED:
        if keyCode == RIGHT and player.walking == False:
            player.dir = "right"
            player.walking = True
        elif keyCode == LEFT and player.walking == False:
            player.dir = "left"
            player.walking = True
        elif keyCode == UP and player.walking == False:
            player.dir = "up"
            player.walking = True
        elif keyCode == DOWN and player.walking == False:
            player.dir = "down"
            player.walking = True

    
