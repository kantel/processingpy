left   = -0.25 # -0.25 -2.25
right  = 0.25  # 0.25 0.75
bottom = -1.0  # -1.0 -1.5
top    = -0.5  # -0.5 1.5

maxlimit = 4.0
maxiter = 100

def setup():
    size(600, 600)
    colorMode(HSB, 255, 100, 100)
    noLoop()

def draw():
    for x in range(width):
        cr = left + x*(right - left)/width
        for y in range(height):
            ci = bottom + y*(top - bottom)/height
            c = complex(cr, ci)
            z = complex(0.0, 0.0)
            for i in range(1, maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    set(x, y, color(0, 0, 0))
                else:
                    # set(x, y, color((i*3)%255, 100, 100))
                    set(x, y, color((255 - i*15)%255, 100, 100))
    println(millis())
