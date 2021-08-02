# Nach einer Idee von Kevin Workman
# (https://happycoding.io/examples/p5js/images/image-palette)

WIDTH = 800
HEIGHT = 640

palette = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
y = 0

def setup():
    global img
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Image Palette")
    img = loadImage("akt.jpg")
    image(img, 0, 0)
    # image(img, width/2, 0)
    noLoop()

def draw():
    global y, img
    for x in range(width/2):
        for y in range(height):
            img_color = img.get(x, y)
            palette_color = get_palette_color(img_color)
            set(x + width/2, y, palette_color)

def get_palette_color(img_color):
    min_distance = 999999    
    img_r = red(img_color)
    img_g = green(img_color)
    img_b = blue(img_color)
    for c in palette:
        palette_r = red(c)
        palette_g = green(c)
        palette_b = blue(c)
        
        color_distance = dist(img_r, img_g, img_b,
                              palette_r, palette_g, palette_b)
        if color_distance < min_distance:
            target_color = c
            min_distance = color_distance
    return(target_color)
