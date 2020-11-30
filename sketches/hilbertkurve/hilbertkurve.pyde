iterations = 7
stroke_len = 600
angle_deg = 90
axiom = 'L'
sentence = axiom
rules = {
    'L': '+RF-LFL-FR+',
    'R': '-LF+RFR+FL-',
}
i = 0

def setup():
    global xo, yo
    size(700, 700)
    this.surface.setTitle("Hilbert-Kurve")
    colorMode(HSB, 360, 100, 100)
    xo, yo = 50, height - 50
    strokeWeight(2)
    noFill()
    generate(iterations)
    noLoop()
 
def draw():
    background(0)
    translate(xo, yo)
    plot(radians(angle_deg))
 
def generate(n):
    global stroke_len, sentence
    for i in range(n):
        stroke_len *= 0.5
        next_sentence = ''
        for c in sentence:
            next_sentence += rules.get(c, c)
        sentence = next_sentence
        
 
def plot(angle):
    global i
    for c in sentence:
        if c == 'F':
            stroke(int(i%360), 50, 100)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
            i += 0.025
            # print(i)
        elif c == '+':
            rotate(angle)
        elif c == '-':
            rotate(-angle)

 
