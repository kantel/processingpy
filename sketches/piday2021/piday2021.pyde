vaporwave10  = ["#8795e8", "#966bff", "#ad8cff", "#c774a9", "#ff6ad5",
                "#ff6a8b", "#ff8b8b", "#392682", "#65323e", "#20de8b"]
pi100        = ("31415926535897932384626433832795028841971693993751058209749445923"
             +  "078164062862089986280348253421170679")

def setup():
    size(275, 275)
    this.surface.setTitle("Happy Pi Day")
    background(234, 218, 184)
    noLoop()

def draw():
    h = 0
    for i in range(len(pi100)):
        if int(pi100[i])%2 != 0:  # Ziffer ungerade
            noStroke()
            fill(vaporwave10[int(pi100[i])])
        else:
            noFill()
            strokeWeight(2)
            stroke(vaporwave10[int(pi100[i])])
        circle((i%10)*25 + 25, h + 25, 20)
        if i > 0 and i%10 == 0:
            h += 25
    print("I did it, Babe!")
    
