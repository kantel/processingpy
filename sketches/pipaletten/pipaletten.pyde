myMagma = ['#000003', '#170F3C', '#430F75', '#711F81', '#9E2E7E', '#CB3E71',
           '#F0605D', '#FC9366', '#FEC78B', '#FBFCBF']
pi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def setup():
    size(275, 275)
    this.surface.setTitle("Pi 100")
    background(55)
    noLoop()

def draw():
    h = 0
    for i in range(len(pi)):
        fill(myMagma[int(pi[i])])
        circle((i%10)*25 + 25, h + 25, 20)
        if i > 0 and i % 10 == 0:
            h += 25
