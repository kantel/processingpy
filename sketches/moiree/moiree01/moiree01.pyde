def setup():
    size(720, 500)

def draw():
    background(220)
    x = 0
    noFill()
    strokeWeight(1)
    for i in range(0, 1000, 3):
        stroke("#800080")
        ellipse(360, 250, i, i)
        stroke("#C80080")
        if i%5:
            ellipse(x, 250, i-500, i-500)
    if x > width:
        x = 0
    else:
        x += 5
