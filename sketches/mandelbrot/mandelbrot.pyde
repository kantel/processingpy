left   = -0.75075 # -2.25
right  = -0.73852 # 0.75
bottom = 0.09898 # -1.5
top    = 0.10816 # 1.5
maxlimit = 4.0
maxiter = 100

def setup():
    size(320, 240)
    background("#ffffff")
    colorMode(HSB, 255, 100, 100)
    # frame.setTitle(u"Mandelbrötchen")
    noLoop()

def draw():
    for x in range(width):
        cr = left + x*(right - left)/width
        for y in range(height):
            ci = bottom + y*(top - bottom)/height
            c = complex(cr, ci)
            z = 0.0
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    set(x, y, color(0, 0, 0))
                else:
                    set(x, y, color((i*48)%255, 100, 100))
        