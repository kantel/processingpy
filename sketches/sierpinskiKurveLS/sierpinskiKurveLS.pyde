iterations = 7
stroke_len = 400
delta = radians(60)
axiom = 'G'
sentence = axiom
rules = {
    'F': 'G-F-G',
    'G': 'F+G+F',
}

def setup():
    global x0, y0
    size(500, 440)
    this.surface.setTitle("Sierpinski-Kurve (mittels L-System)")
    x0, y0 = 230, height - 140
    strokeWeight(2)
    noFill()
    generate(iterations)
    noLoop()
 
def draw():
    background(234, 218, 184)
    rotate(radians(30))
    translate(x0, y0)
    colorMode(HSB, 360, 255, 255)
    plot(delta)
 
def generate(n):
    global stroke_len, sentence
    for i in range(n):
        stroke_len *= 0.5
        next_sentence = ''
        for c in sentence:
            next_sentence += rules.get(c, c)
        sentence = next_sentence
         
def plot(angle):
    k = 0
    for c in sentence:
        if c == 'F' or c == 'G':
            stroke(int(k%360), 255, 180)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
            k += 0.25
        elif c == '+':
            rotate(angle)
        elif c == '-':
            rotate(-angle)

 
