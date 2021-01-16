import math

left   = -2.25 # -2.25 -0.25
right  = 0.75  # 0.75 0.25
bottom = -1.5  # -1.5 -1.0
top    = 1.5  # 1.5 -0.5

maxlimit = 4.0
maxiter = 100

def setup():
    size(600, 600)
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
                    log_iter = math.log(i)
                    r = int(255*(1 + math.cos(3.32*log_iter))/2)
                    g = int(255*(1 + math.cos(0.774*log_iter))/2)
                    b = int(255*(1 + math.cos(0.412*log_iter))/2)
                    set(x, y, color(r, g, b))
    println(millis())
        
