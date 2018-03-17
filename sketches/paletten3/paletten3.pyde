"""
Männerpaletten
"""

w = 64
h = 16

def setup():
    size(480, 530)
    noLoop()
    
def draw():
    background("#2b3e50")
    
    fill(255, 0, 0)
    rect(10, 10, w, h)
    fill(255)
    text("Schraubendrehergriffrot", w + 20, 22)
    fill(250, 128, 114)
    rect(10, 10 + h, w, h)
    fill(255)
    text("Pflaster", w + 20, 40)
    fill(219, 112, 147)
    rect(10, 10 + 2*h, w, h)
    fill(255)
    text("Rosa", w + 20, 57)
