font = None
pangramme = [u"Zwölf Boxkämpfer jagen Eva quer über den großen Sylter Deich.",
             u"Jörg bäckt quasi zwei Haxenfüße vom Wildpony.",
             u"Falsches Üben von Xylophonmusik quält jeden größeren Zwerg.",
             u"Schweißgequält zündet Typograph Jakob verflixt öde Pangramme an.",
             u"Vom Ödipuskomplex maßlos gequält, übt Wilfried zyklisches Jodeln.",
             u"Asynchrone Bassklänge vom Jazzquintett sind nix für spießige Löwen."]
             
colors = ["#cd0000", "#008b00", "#ffff00", "#a52a2a", "#ff00ff", "#00ffff"]

def setup():
    global x, index
    frame.setTitle("Parade der Pangramme")
    size(800, 100)
    font = createFont("Barrio-Regular.ttf", 64)
    textFont(font)
    x = width
    index = 0

def draw():
    global x, index
    background(0)
    fill(colors[index])
    textAlign(LEFT)
    text(pangramme[index], x, 80)
    x -= 3
    w = textWidth(pangramme[index])
    if (x < -w):
        x = width
        index = (index+1) % len(pangramme)