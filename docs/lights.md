# Licht und Schatten

[![Screenshot](images/lichtundschatten.jpg)](https://www.flickr.com/photos/schockwellenreiter/32593587580/)

## Quellcode

~~~python
lightMode = 0
lightDirection = 0

def setup():
    size(640, 480, P3D)
    frame.setTitle("Licht und Schatten")

def draw():
    global lightMode, lightDirection
    background(0)
    
    # Lichter setzen
    if lightMode == 0:
        noLights()
    elif lightMode == 1:
        lights()
    elif lightMode == 2:
        if lightDirection == 0:
            directionalLight(255, 128, 0, 0, -1, 0) # up
        elif lightDirection == 1:
            directionalLight(0, 255, 0, 1, 0, 0)    # right
        elif lightDirection == 2:
            directionalLight(255, 0, 255, 0, 1, 0)  # down
        elif lightDirection == 3:
            directionalLight(0, 255, 255, -1, 0, 0) # left
    elif lightMode == 3:
        ambientLight(0, 255, 255)
    elif lightMode == 4:
        pointLight(255, 255, 0, 100, height*0.3, 100)
    elif lightMode == 5:
        spotLight(128, 255, 128, 800, 20, 300, -1, .25, 0, PI, 2)
    else:
        noLights()
    
    # Kugel und Box zeichnen
    with pushMatrix():
        translate(width/2, height/2)
        with pushMatrix():
            rotateY(radians(frameCount))
            fill(255)
            if lightMode == 1:
                fill(151, 255, 255)
            noStroke()
            sphere(160)
        with pushMatrix():
            rotateZ(radians(frameCount))
            rotateX(radians(frameCount/2.0))
            fill(255)
            if lightMode == 1:
                fill(0, 0, 139)
            noStroke()
            box(240)
            
def keyPressed():
    global lightMode, lightDirection
    if key == "n":
        lightMode = 0            # no lights
    elif key == "l":
        lightMode = 1            # lights
    elif key == "d":
        lightMode = 2            # directional light
    elif key == "a":
        lightMode = 3            # ambient light
    elif key == "p":
        lightMode = 4            # point light
    elif key == "s":
        lightMode = 5            # spot light
    
    if key == CODED:
        if keyCode == UP:
            lightDirection = 0
        elif keyCode == RIGHT:
            lightDirection = 1
        elif keyCode == DOWN:
            lightDirection = 2
        elif keyCode == LEFT:
           lightDirection = 3
~~~