from unicornrainbow import UnicornRainbow

def setup():
    global unicorn
    size(920, 360)
    this.surface.setTitle("Coding Train Unicorn Rainbow")
    unicorn = UnicornRainbow()    

def draw():
    global unicorn
    background(10, 52, 101)
    unicorn.add_rainbow_stripes(200, color(255, 0, 0))
    unicorn.update()
    unicorn.show()
