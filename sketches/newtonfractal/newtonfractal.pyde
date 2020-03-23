xa = -1.0
xb = 1.0
ya = -1.0
yb = 1.0

maxIt = 20
h = 1e-6
eps = 1e-3

def setup():
    size(512, 512)
    this.surface.setTitle("Newton Fractal")
    noLoop()

def draw():
    img = createImage(width, height, RGB)
    img.loadPixels()
    for y in range(height):
        zy = y*(yb - ya)/(height - 1) + ya
        for x in range(width):
            zx = x*(xb - xa)/(width - 1) + xa
            z = complex(zx, zy)
            for i in range(maxIt):
                dz = (f(z + complex(h, h)) - f(z))/complex(h, h)
                z0 = z - f(z)/dz
                if abs(z0 - z) < eps:
                    break
                z = z0
            for j in range(len(img.pixels)):
                img.pixels[j] = color(i % 5 * 64, i % 17 * 16, i % 9 * 32)
    img.updatePixels()
    image(img, 0, 0)
    print("I did it, Babe")
    
def f(z):
    return (z*z*z - 1)
