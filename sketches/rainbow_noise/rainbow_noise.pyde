colors = [color(146, 82, 161), color(240, 99, 164), color(49, 197, 244),
          color(248, 239, 34), color(248, 158, 80), color(240, 80, 37),
          color(129, 122, 198)]
a = 10    # alpha

def setup():
    global t, i, pg
    size(640, 480)
    this.surface.setTitle("Perlin Noise Worm")
    pg = createGraphics(width, height)
    t = PVector(0, 10000)
    i = 0

def draw():
    global t, i, pg
    n1 = noise(t.x)
    n2 = noise(t.y)
    x = map(n1, 0, 1, 0, width)
    y = map(n2, 0, 1, 0, height)
    with pg.beginDraw():
        pg.background(98, 199, 119, a)
        pg.fill(colors[i])
        pg.circle(x, y, 32)
    image(pg, 0, 0)
    t.x += 0.01
    t.y += 0.01
    if frameCount%10 == 0:
        i += 1
        if i == len(colors):
            i = 0
    
