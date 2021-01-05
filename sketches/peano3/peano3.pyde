add_library('Turtle')
import math

num_gen = 4
len_seg = 4 
a = 90  # Winkel
axiom = "S"
sentence = axiom
rules = {"S": "SFZFS+F+ZFSFZ-F-SFZFS",
         "Z": "ZFSFZ-F-SFZFS+F+ZFSFZ",
}


def setup():
    global p
    size(400, 400)
    this.surface.setTitle("SZ-Peano-Kurve")
    background(50)
    strokeWeight(1)
    stroke(150, 255, 100)
    p = Turtle(this)
    p.right(a)
    generate(num_gen)
    noLoop()

def draw():
    p.penUp()
    p.goToPoint(40, height-40)
    p.penDown()
    plot(p)
    print("I did it, Babe")
    
def generate(n):
    global len_seg, sentence
    for i in range(n):
        # len_seg *= 0.5
        next_sentence = ""
        for c in sentence:
            next_sentence += rules.get(c, c)
        sentence = next_sentence
    # print(sentence)
        
def plot(p):
    for c in sentence:
        if c == "F":
            p.forward(len_seg)
        elif c == "+":
            p.left(a)
        elif c == "-":
            p.right(a)
