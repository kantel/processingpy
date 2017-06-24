import random as r

def setup():
    size(800, 640)
    output =open("forrest.tsv", "w")
    output.write("type\tx\ty\n")
    ellipseMode(CORNER)
    for y in range(0, height, 16):
        for x in range(0, width, 16):
            forrestType = str(r.randint(1, 4))
            output.write(forrestType + "\t" + str(x) + "\t" + str(y) + "\n")
            ellipse(x, y, 16, 16)
    output.close()
