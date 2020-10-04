import cmath

imgx = 512
imgy = 512

# Drawing area
# xa = 1.126
xa = -2.0
xb = 2.0
ya = -2.0
yb = 2.0
# ya = -1.0
# yb = 1.0

maxIt = 20 # max iterations allowed
h = 1e-6   # stepsize for numerical derivative
eps = 1e-3 # max error allowed

def f(z):
    # return cmath.sin(z)
    # return z*z*z*z*z*z - 1.0
    return z*(z*z*z*z*z*z - 1.0)

def setup():
    global img
    size(imgx, imgy)
    this.surface.setTitle("Newton Fractal (2)")
    img = createImage(width, height, RGB)
    noLoop()

def draw():
    global img
    loadPixels()
    img.loadPixels()
    for y in range(imgy):
        zy = y*(yb - ya)/(imgy - 1) + ya
        for x in range(imgx):
            zx = x*(xb - xa)/(imgx - 1) + xa
            z = complex(zx, zy)
            for i in range(maxIt):
                # Complex numerical derivative
                dz = (f(z + complex(h, h)) - f(z))/complex(h, h)
                if dz != 0:
                    z0 =  z - f(z)/dz     # Newton iteration
                if abs(z0 - z) < eps:
                    # Stop when close enough to any root
                    break
                z = z0
                
            loc = x + y*width
            # pixels[loc] = color(i%5*64, i%9*32, i%17*16)   
            pixels[loc] = color(i%5*64, i%17*16, i%9*32)
    updatePixels()
    print("I did it, Babe!")
