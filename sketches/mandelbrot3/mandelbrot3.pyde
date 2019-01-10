# Diese Parameter ergeben die komplette Mandelbrotmenge
# left   = -2.25
# right  = 0.75
# bottom = -1.5
# top    = 1.5
# maxlimit = 2.0
# maxiter = 20

# Diese Parameter sind eine Reise ins Seepfedchental
left   = -0.74647
right  = -0.74501
bottom = 0.1046
top    = 0.105694
maxlimit = 2.0
maxiter = 200


def setup():
    size(400, 400)
    background("#ffffff")
    this.surface.setTitle(u"Mandelbrötchen")
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
                    set(x, y, color(i % 17 * 16, i % 9 * 32, i % 5 * 64))
