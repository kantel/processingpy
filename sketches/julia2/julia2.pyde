left   = -2.0
right  = 2.0
bottom = 2.0
top    = -2.0
maxlimit = 2.0
maxiter = 25
c = complex(-0.70176, -0.3842)

def setup():
    size(400, 400)
    background("#555ddd")
    colorMode(HSB, 1)
    noLoop()

def draw():
    for x in range(width):
        cr = left + x*(right - left)/width
        for y in range(height):
            ci = bottom + y*(top - bottom)/height
            z = complex(cr, ci)
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter-1):
                    set(x, y, color(0))
                else:
                    set(x, y, color(sqrt(float(i)/maxiter), 100, 100))
    println(millis())
                