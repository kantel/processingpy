add_library('Turtle')
import math

num_gen = 4
len_seg = 6 
a = 22.5  # Winkel
axiom = "F"
sentence = axiom
rules = {"F": "FF-[-F+F+F]+[+F-F-F]"}


def setup():
    global p
    size(400, 400)
    this.surface.setTitle("Lindenmayer Tree 1")
    background(50)
    strokeWeight(1)
    stroke(150, 255, 100)
    p = Turtle(this)
    generate(num_gen)
    noLoop()

def draw():
    p.penUp()
    p.goToPoint(width/2, height - 20)
    p.penDown()
    plot(p)
    print("I did it, Babe")
    
def generate(n):
    global sentence
    for i in range(n):
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
            p.right(a)
        elif c == "-":
            p.left(a)
        elif c == "[":
            p.push()
        elif c == "]":
            p.pop()
    
    
