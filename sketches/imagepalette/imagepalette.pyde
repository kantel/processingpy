# Nach einer Idee von Kevin Workman
# (https://happycoding.io/examples/p5js/images/image-palette)

WIDTH = 800
HEIGHT = 640

genuary23 = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
riley2 = [color(230, 230, 230), color(235, 200, 55), color(115, 165, 215),
          color(155, 195, 80), color(230, 135, 170), color(230, 80, 70),  
          color(65, 80, 150)]
codingtrain = ["#f05025", "#f89e50", "#f8ef22", "#31c5f4", "#f063a4",
               "#9252a1", "#817ac6", "#62c777"]
superColors = ["#df691b", "#5cb85c", "#5bc0de",
               "#f0ad4e", "#d9534f", "#4e5d6c"]

def setup():
    global img
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Image Palette")
    img = loadImage("akt.jpg")
    image(img, 0, 0)
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
    for c in superColors:
        palette_r = red(c)
        palette_g = green(c)
        palette_b = blue(c)
        
        color_distance = dist(img_r, img_g, img_b,
                              palette_r, palette_g, palette_b)
        if color_distance < min_distance:
            target_color = c
            min_distance = color_distance
    return(target_color)
