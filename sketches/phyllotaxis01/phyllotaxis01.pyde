magma11 = ['#000003', '#140D35', '#3B0F6F', '#63197F', '#8C2980', '#B53679', '#DD4968',
           '#F66E5B', '#FD9F6C', '#FDCD90', '#FBFCBF']
# magma10 = ['#000003', '#170F3C', '#430F75', '#711F81', '#9E2E7E', '#CB3E71', '#F0605D',
#            '#FC9366', '#FEC78B', '#FBFCBF']
# magma9 = ['#000003', '#1B1044', '#4F117B', '#812581', '#B53679', '#E55063', '#FB8660',
#           '#FEC286', '#FBFCBF']
# magma8 = ['#000003', '#221150', '#5D177E', '#972C7F', '#D1426E', '#F8755C', '#FEB97F',
#           '#FBFCBF']
# magma7 = ['#000003', '#2B115E', '#711F81', '#B53679', '#F0605D', '#FEAE76', '#FBFCBF']
# magma6 = ['#000003', '#3B0F6F', '#8C2980', '#DD4968', '#FD9F6C', '#FBFCBF']
# magma5 = ['#000003', '#4F117B', '#B53679', '#FB8660', '#FBFCBF']

n = 0
c = 6

def setup():
    size(800, 600)
    this.surface.setTitle("Phyllotaxis 1")
    background(235, 215, 182)

def draw():
    global n
    a = n * radians(137.5)
    r = c * sqrt(n)
    x = r*cos(a)
    y = r*sin(a)
    
    fill(magma11[(n%11) + 0])
    translate(width/2, height/2)
    circle(x, y, 8)
    n += 1
    if n > 2095:
        print("I did it, Babe!")
        saveFrame("magma11.png")
        noLoop()
