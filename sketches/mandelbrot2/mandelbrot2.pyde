# Das Mandelbrot-Set als Pixel-Array nach Daniel Shiffman

maxlimit = 4.0
maxiter = 100

def setup():
    size(600, 600)
    colorMode(HSB, 255, 100, 100)
    noLoop()

def draw():
    background("#ffffff")
    w = 3.0
    h = (w*height/width)
    xmin = -w/2.0 - 0.75
    ymin = -h/2.0
    loadPixels()
    xmax = xmin + w
    ymax = ymin + h
    dx = (xmax - xmin)/(width)
    dy = (ymax - ymin)/(height)
    y = ymin
    for j in range(height):
        x = xmin
        for i in range(width):
            n = 0
            z = 0.0
            for n in range(maxiter):
                c = complex(x, y)
                z = (z**2) + c
                if abs(z) > maxlimit:
                    break
                if n == maxiter - 1:
                    pixels[i + j*width] = color(0, 0, 0)
                else:
                    pixels[i + j*width] = color((n*48)%255, 100, 100)
            x += dx
        y += dy
    updatePixels()
    println(millis())
        