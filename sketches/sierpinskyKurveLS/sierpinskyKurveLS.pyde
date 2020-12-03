iterations = 7
stroke_len = 600
delta = radians(60)
axiom = 'G'
sentence = axiom
rules = {
    'F': 'G-F-G',
    'G': 'F+G+F',
}

def setup():
    global x0, y0
    size(700, 700)
    this.surface.setTitle("Sierpinski-Kurve (mittels L-System)")
    colorMode(HSB, 360, 100, 100)
    x0, y0 = 340, height - 210
    strokeWeight(2)
    noFill()
    generate(iterations)
    noLoop()
 
def draw():
    background(0)
    rotate(radians(30))
    translate(x0, y0)
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
            stroke(int(k%360), 50, 100)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
            k += 0.25
        elif c == '+':
            rotate(angle)
        elif c == '-':
            rotate(-angle)

 
