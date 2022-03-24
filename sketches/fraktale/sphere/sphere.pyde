import math
 
xscreen = 500
yscreen = 500
grid = 500
# dx = 250
# dy = 250
maximum_iteration = 100
edge = 10
cr = 0
ci = 0
alfa = 30
beta = - 60
border = 100.0
xglo = 0.0
yglo = 0.0
zglo = 0.0
column, row = 3, 3
xaxemat = [[0 for _ in range(row)] for _ in range(column)]
yaxemat = [[0 for _ in range(row)] for _ in range(column)]
 
# ??? METHOD for class appleSphereProcessing
def domath():
    global x0, y0, ci, cr, border, maximum_iteration, iteration_counter
    iteration_counter = 0
    # print(x0, y0, iteration_counter)
    xhigh2 = x0 * x0
    yhigh2 = y0 * y0
    distance_square = xhigh2 + yhigh2
    while (distance_square < border and iteration_counter < maximum_iteration):
        iteration_counter += 1
        # print(distance_square)
        y0 = 2 * x0 * y0 - ci
        x0 = xhigh2 - yhigh2 - cr
        xhigh2 = x0 * x0
        yhigh2 = y0 * y0
        distance_square = xhigh2 + yhigh2
 
def initmat():
    global alfa, beta
    alf = alfa * PI / 180.0
    bet = beta * PI / 180.0
    xaxemat[0][0] = 1.0
    xaxemat[0][1] = 0.0
    xaxemat[0][2] = 0.0
    xaxemat[1][0] = 0.0
    xaxemat[1][1] = math.cos(alf)
    xaxemat[1][2] = math.sin(alf)
    xaxemat[2][0] = 0.0
    xaxemat[2][1] = -math.sin(alf)
    xaxemat[2][2] = math.cos(alf)
    yaxemat[0][0] = math.cos(bet)
    yaxemat[0][1] = 0.0
    yaxemat[0][2] = math.sin(bet)
    yaxemat[1][0] = 0.0
    yaxemat[1][1] = 1.0
    yaxemat[1][2] = 0.0
    yaxemat[2][0] = -math.sin(bet)
    yaxemat[2][1] = 0.0
    yaxemat[2][2] = math.cos(bet)
    # print(yaxemat[2][2])
 
# ??? METHOD for class appleSphereProcessing
def multiplyIt():
    global xglo, yglo, zglo, yaxemat, yaxemat 
    xzwi = yaxemat[0][0] * xglo + yaxemat[0][1] * yglo + yaxemat[0][2] * zglo
    yzwi = yaxemat[1][0] * xglo + yaxemat[1][1] * yglo + yaxemat[1][2] * zglo
    zzwi = yaxemat[2][0] * xglo + yaxemat[2][1] * yglo + yaxemat[2][2] * zglo
    xglo = xaxemat[0][0] * xzwi + xaxemat[0][1] * yzwi + xaxemat[0][2] * zzwi
    yglo = xaxemat[1][0] * xzwi + xaxemat[1][1] * yzwi + xaxemat[1][2] * zzwi
    zglo = xaxemat[2][0] * xzwi + xaxemat[2][1] * yzwi + xaxemat[2][2] * zzwi
 
# ??? METHOD for class appleSphereProcessing
def setscreenpoint(xw, yw):
    global xsceen, yscreen
    point(xw, yscreen - yw)
 
# ??? METHOD for class appleSphereProcessing
def find_cr_ci(x, y):
    global xsceen, yscreen, xglo, yglo, zglo, radius, cr, ci
    if (sq(x - xscreen / 2) + sq(y - yscreen / 2) > sq(xscreen / 2)):
        return(False)
    else:
        xglo = (1.0*x - radius) / radius
        yglo = (1.0*y - radius) / radius
        zglo = -math.sqrt(abs(1.0 - (sq(xglo) + sq(yglo))))
        multiplyIt()
        # print("Exit multiplay")
        if (zglo == 1.0):
            cr = 0.0
            ci = 0.0
        else:
            cr = xglo / (1.0 - zglo)
            ci = yglo / (1.0 - zglo)
        return(True)
 
def mapping():
    global xsceen, yscreen, x0, y0, iteration_counter, edge, maximum_iteration
    # print(xscreen, yscreen)
    for y in range(yscreen + 1):
        for x in range(xscreen + 1):
            y0 = 0
            x0 = 0
            # print("noch nix gefunden")
            if (find_cr_ci(x, y)):
                # print("enter domath")
                domath()
                # print("exit domath")
                # print(iteration_counter)
                if (((iteration_counter % 2 == 1) and (iteration_counter <= edge))
                     or (iteration_counter == maximum_iteration)):
                    # print("enter setscreenpoint")
                    setscreenpoint(x, y)
                    
    milli = millis()
    # print("Millis = ", milli)
    picturename = "AM_3D" + str(milli) + ".png"
    # save(picturename)
    # print("Fertig")
 
# ??? METHOD for class appleSphereProcessing
def setup():
    global xscreen, yscreen, radius
    size(xscreen, yscreen)
    this.windowTitle(u"Mandelbrötchen auf einer Kugel 🐍")
    this.windowMove(1400, 30)
    radius = xscreen / 2
    colorMode(RGB, 255)
    initmat()
    background(255)
    noLoop()
    
def draw():
    mapping()
    print(u"I did it, Babe! 🐍")
