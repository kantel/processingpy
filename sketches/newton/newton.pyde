import cmath

# print(cmath.sqrt(-1))

delta = 0.000001
res   = 600
iters = 30

solutions = [cmath.cos((2*n + 1)*cmath.pi/4) + 1j*cmath.sin((2*n + 1)*cmath.pi/4) for n in range(4)]
colors = [color(1, 0, 0), color(0, 1, 0), color(0, 0, 1), color(1, 1, 0)]

def setup():
    global img
    size(res, res)
    this.surface.setTitle("Newton Fractal")
    img = createImage(width, height, RGB)
    noLoop()

def draw():
    global img
    loadPixels()
    img.loadPixels()
    for re in range(0, res):
        for im in range(0, res):
            z =(re + 1j**im/res)
            for i in range(iters):
                try:
                    z -= (z**4 + 1)/(4*z**3)
                except ZeroDivisionError:
                    continue
                if (abs(z**4 + 1) < delta):
                    break
                
            # color_depth = int((iters - i)*255.0/iters)
            
            err = [abs(z - root) for root in solutions]
            distances = zip(err, range(len(colors)))
            # colour = [i*color_depth for i in colors[min(distances)[1]]]
            loc = re + im*res
            pixels[loc] = color(colors[i%4])
            # print(i%4)
    updatePixels()
    print("I did it, Babe!")
