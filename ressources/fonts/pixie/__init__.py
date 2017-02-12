# Pixie - last updated for NodeBox 1.9.3
# Author: Tom De Smedt <tomdesmedt@organisms.be>
# Manual: http://nodebox.net/code/index.php/Pixie
# Copyright (c) 2007 by Tom De Smedt.
# See LICENSE.txt for details.

# Remember to install the fonts before running the library.

from random import choice
from nodebox.graphics import CENTER, CORNER, CMYK
from nodebox.util import random, choice

SPACING = 1.2
def spacing(x=1.2):
    
    """Sets the lineheight or linespacing 
    for a pixie text paragraph().
    """
    
    global SPACING
    SPACING = x
    
lineheight = spacing
    
COLOR = (0.8, 0.4, 0.0, 0.4)
def color(c=0.8, m=0.4, y=0.0, k=0.4):
    
    """Sets the text color 
    for a pixie text paragraph().
    """
    
    global COLOR
    COLOR = (c, m, y, k)
    
KEYWORDS = []
KEYWORDS_ALL = False
def keywords(list=[], all=False):
    
    """Sets a list of keywords pixie should mark as important.
    
    The paragraph() command uses this list to determine which
    words should be drawn within a border. When all=True,
    it draws any occurence of a keyword in a border, 
    but by default only the first one.
    """
    
    #If list is a string, convert it to a list.
    from types import StringType
    if type(list) == StringType: list = [list]
    
    global KEYWORDS, KEYWORDS_ALL
    KEYWORDS = list
    KEYWORDS_ALL = all

def border(x, y, width, pt=20, slant=0.5):
    
    """Draws a handrwritten rectangle at (x,y) with given width.
    
    This command is usually called from within 
    the pixie text paragraph() command as a callback 
    that draws borders around words.
    """
    
    _ctx.transform(CENTER)
    
    #Somewhere in the Pixie-Dingbats font are rectangle characters.
    glyph = choice(("A", "B"))
    
    #A thing about borders is that you
    #usually draw one, and then move your pen around on those lines,
    #so the border becomes really thick and visible.
    #The same is done here with a for-loop.
    for i in range(random(1,5)):    
    
        glyphwidth = random(2.3, 2.4)
    
        _ctx.push()
        _ctx.scale(width/(glyphwidth*pt), random(1.1, 1.2))
        _ctx.skew(slant*7 + random(8))
        _ctx.rotate(random(-slant,0))
        
        f = width/(glyphwidth*pt)
        f = f*glyphwidth*pt - glyphwidth*pt
        f = f/2
    
        _ctx.font("Pixie-Dingbats", pt)
        _ctx.text(glyph, x+f, y, width)

        _ctx.pop()
        
def mistake(txt, x, y, pt=20, slant=0.5):
    
    """Draws a piece of pixie text in strikethrough.
    
    This command is used as a callback from paragraph(),
    inserting some errrors in the paragraph flow
    here and there.
    """
    
    #Somewhere in the Pixie-Dingbats font are strikethrough characters.
    glyph = choice(("C", "D"))
    
    #Guess the length of txt set in the paragraph() command.
    #The dx is a visual correction, so the typo appears not
    #too close to the previous word, and not too close to the next.
    width = len(txt) * random(pt*0.4, pt*0.5)
    dx = width/len(txt) * 0.5

    #Create a typo in the txt string
    #At the current position, draw the typo txt in paragraph().
    char = choice(txt[min(len(txt)-1,1):])
    txt = txt.replace(char, choice("abcdefghijklmnopqrstuvwxyz"))
    paragraph(txt, x-dx, y, width*2, pt, slant)
    
    #Now, strikethrough the typo.
    _ctx.push()
    _ctx.scale(width/(pt*2.5), random(0.7, 1.3))
    _ctx.rotate(random(-3,3))
    _ctx.font("Pixie-Dingbats")
    _ctx.text(glyph, x-dx, y)
    _ctx.pop()
    
    return width

DISTRACTION = 0.05
def distraction(d=0.05):
    
    """Determine how many writing errors pixie makes.
    
    Distraction ranges between 0.0 and 1.0,
    setting how often mistake() is called from paragraph().
    The more distracted pixie gets, the more words will be
    scribbled through.
    
    Making mistakes is a recursive process: corrections of
    mistakes might become mistakes themselves, and so on.
    Setting a high distraction on a long paragraph may take
    a while to draw.
    
    """
    
    global DISTRACTION
    DISTRACTION = max(0,min(d,1))

def underline(x, y, width, pt=20):
    
    """Draws a horizontal line.
    
    Draws a horizontal line at (x,y) with the given width.
    This command serves as a callback for paragraph()
    to underline a paragraph of text, just as Tom does.
    """
    
    _ctx.font("Pixie-Dingbats", pt)
    
    y += random(pt*0.5)
    
    #In handwriting, when you stress something by underlining it,
    #you never just put one measely line. This is simulated here
    #by drawing several lines on top of each other, like scratching.
    for i in range(random(1,2)):
        line(x, y+random(pt*0.1), x+width+random(pt), y+random(pt*0.1))
    
    #Little construction banners to top off
    #that really you-just-gotta-have Tom handwriting!
    if random(100)>94:
        _ctx.scale(random(0.9,1.1))
        under_construction = "L"
        _ctx.text(under_construction, x+width-1.5*pt, y-pt*0.2)
    
    #Return the vertical offset of the cursor.
    return y
    
def height(txt, width, pt=20):
    
    """Returns the height of paragraph() with txt, width and pt.
    
    This command gives "some" idea of the height,
    with an average deviation of 20%. 
    
    """
    
    dx = 0
    dy = 0
    
    for i in range(len(txt)):
        
        dx += random(pt*0.3, pt*0.5)
        dy += random(-pt*0.05, pt*0.05)
        
        if dx > width and txt[i] in (" ", ".", ","):
            dx = random(-pt*0.1, pt*0.2)
            dy += random(pt*0.7, pt*0.9) * SPACING
    
    dy += random(pt*0.7, pt*0.9) * SPACING        
    return dy
    
textheight = height
    
def paragraph(txt, x, y, width, pt=20, slant=0.5, line=False, serif=False):
    
    """Draws a paragraph of Tom's handwriting.
    
    Draws the string txt in Tom's handwriting,
    positioned at x, y with the given width, font size pt.
    The slant argument controls the speed at which Tom writes.
    
    The lineheight setting of spacing() is taken into account,
    and words supplied to keywords() are framed in a border.
    The text is drawn in color().
    
    The serif parameter defines serif characters
    to be used in the paragraph.
    
    """
    
    #Ensure that all pixiekeywords() are found,
    #even in a single word pixie text.
    txt += " "
    
    keywords_done = []
    keyword_end = -1
    
    _ctx.transform(CENTER)
    
    dx = x
    dy = y
    
    for i in range(len(txt)):
        
        _ctx.push()
        
        #There is a world of difference between handwritten glyphs in a font,
        #and handwriting. Handwriting doesn't stay on a straight line,
        #two characters never look identical, the pen presses down harder
        #now and then. The same is simulated with scale, skew and rotate.
        _ctx.scale(random(0.9, 1.1), random(0.9, 1.1))
        _ctx.skew(slant*10 + random(8))
        _ctx.rotate(slant*-2)
        
        #Set color to pixiecolor(), varying the K value
        #to simulate pen pressure.
        _ctx.colormode(CMYK)
        c, m, y, k = COLOR
        _ctx.fill(c, m, y, k+random(-0.2,0.2))
        
        #Draw the current character in txt in the given fontsize.
        #Use a bold font for text in a border (see below).
        fonts = ("Pixie","Pixie-SemiBold")
        if serif: fonts += ("Pixie-Light",)
        _ctx.font(choice(fonts), pt)
        if i <= keyword_end: _ctx.font("Pixie-Bold", pt)
        try: _ctx.text(txt[i].upper(), dx, dy+random(slant*pt*0.1))
        except: pass
        
        _ctx.pop()        
        
        #Traverse the list of keywords,
        #if we are at the beginning of one of those words,
        #set a x-coordinate flag.
        for keyword in KEYWORDS:
            j = i+len(keyword)
            #No need to continue if only the first encounter of a keyword
            #needs to be processed.
            if KEYWORDS_ALL == False and keyword in keywords_done: pass
            elif txt[i:j].lower() == keyword.lower():
                keywords_done.append(keyword)
                keyword_x = dx
                keyword_end = j
                
        #When the end of that word is reached,
        #we know its width and can draw a border around it.
        if i == keyword_end:
            border(keyword_x, dy, dx-keyword_x, pt, slant)
                   
        #Advance the cursor to the next character in txt.
        dx += random(pt*0.3, pt*0.5)
        dy += random(-pt*0.05, pt*0.05)
        
        #Advance to a new line if this line exceeds the width,
        #and is at the end of a word.
        #The spacing() lineheight is taken into account.
        if txt[i] == "\n" or (dx-x > width and txt[i] in (" ", ".", ",")):
            dx = x + random(-pt*0.1, pt*0.2)
            dy += random(pt*0.7, pt*0.9) * SPACING
            
        #Before drawing a nice new word, it may be possible
        #that a small error is made, after all, if we write
        #a text by hand some thing will have to be corrected as well.
        if txt[i] in (" ", ".", ",") and random()<DISTRACTION/2.0:
            dx += mistake(txt[i:i+random(3,5)], dx, dy, pt, slant)
    
    if line:
        #Draw a line underneath the paragraph of text.
        dy = underline(x, dy, width, pt)
    
    #Return the offset of the cursor.
    dy += (random(pt*0.7, pt*0.9) * SPACING) * 0.75
    return (dx,dy)

text = paragraph

def heading(txt, x, y, width, pt=30, slant=0.0):
    
    """Draws a title heading in Tom's handwriting.
    
    Draws the string txt in Tom's handwriting,
    positioned at x, y with the given width, font size pt.
    The slant argument controls the speed at which Tom writes.
    
    The lineheight setting of spacing() is taken into account.
    The text is drawn in color().
    """
    
    txt = txt.upper()
    
    _ctx.transform(CENTER)
    
    dx = x
    dy = y
    
    for i in range(len(txt)):
        
        _ctx.push()
        
        #Vary each individual character
        #to simulate handwriting.
        _ctx.scale(random(0.9, 1.5), random(0.9, 1.5))
        _ctx.skew(slant*10 + random(8))
        _ctx.rotate(slant*-2)
        
        #Set color to pixiecolor(), varying the K value
        #to simulate pen pressure.
        _ctx.colormode(CMYK)
        c, m, y, k = COLOR
        _ctx.fill(c, m, y, k+random(-0.0,0.3))

        #Draw the current character in txt in the given fontsize.
        _ctx.font("Pixie-Fat", pt)
        _ctx.text(txt[i], dx, dy, width)
        
        #Advance the cursor to the next character in txt.
        dx += random(pt*1.4, pt*1.5)
        dy += random(-pt*0.1, pt*0.1)

        #Advance to a new line if this line exceeds the width,
        #and is at the end of a word.
        #The spacing() lineheight is taken into account.        
        if txt[i] == "\n" or (dx-x > width and txt[i] in (" ", ".", ",")):
            dx = x + random(-pt*0.1, pt*0.2)
            dy += random(pt*1.3, pt*1.6) * SPACING
            
        _ctx.pop()
    
    #To top it off, draw a cool doodle next to the heading.
    if random(100) > 97:
        sprite(dx+pt*0.3, dy, pt=pt*0.9)

    #Return the offset of the cursor.    
    dy += random(pt*0.7, pt*0.9) * SPACING        
    return (dx,dy)

def list(title, list, x, y, width, pt=20, slant=0.5):
    
    """Draws a small list scheme.
    
    Draws a list scheme, with centrally, the title in a border.
    Arrows branch from the title to words in the given list.
    
    """
    
    from math import radians, sin, cos
    
    #Draw the title in a border using pixie().
    #A space is added to the title to ensure it draws a border around it.
    spacing(1.0)
    keywords(title.split(" "))
    txt = title+" "
    x_end, y = paragraph(txt, x, y, width, pt, slant)
    y -= pt/1.25
    
    for i in range(len(list)):
        
        _ctx.push()
        
        #Somewhere in the Pixie-Dingbats font are arrow characters.
        glyph = choice(("E", "F", "G"))
        
        #Set color to pixiecolor(), varying the K value
        #to simulate pen pressure.
        _ctx.colormode(CMYK)
        cc, mc, yc, kc = COLOR
        _ctx.fill(cc, mc, yc, kc+random(-0.1,0.2))
        
        #Draw an arrow branching from the title.
        _ctx.transform(CORNER)
        _ctx.push()
        _ctx.translate(x+pt/2,y)

        a = random(-40,-35)*(i+1)
        _ctx.rotate(a)       
        
        f = random(1.0,1.5)
        _ctx.scale(f, max(1,f/2))

        _ctx.font("Pixie-Dingbats", pt)
        _ctx.text(glyph, pt/3, pt*0.35)
        _ctx.pop()
        
        #Good old-fashioned geometry to
        #calculate where we put the list item next to an arrow.
        #Play around with the numbers to get the position exactly right.
        glyphwidth = 4.5
        dx = cos(radians(a)) * pt * glyphwidth * f
        dy = sin(radians(a)) * pt * glyphwidth * (f/1.5)        
        if a % 360 > 0 and a % 360 < 180: dy += pt*1.5
        if a % 360 > 240 and a % 360 < 360: dy -= pt/2
        if a % 360 > 80 and a % 360 < 110: dy += pt/2
        _ctx.transform(CENTER)
        paragraph(list[i], x+dx, y-dy+pt, width/2, pt*0.75)
        
def sprite(x, y, pt=40):
    
    """Draws an imbecile.
    
    Draws a doodle sprite at (x,y),
    varying legs, faces, bodies, and more.
    """
    
    _ctx.transform(CENTER)
    
    #Set color to pixiecolor(), varying the K value
    #to simulate pen pressure.
    _ctx.colormode(CMYK)
    cc, mc, yc, kc = COLOR
    _ctx.fill(cc, mc, yc, kc+random(-0.2,0.2))
    
    #Somewhere in the Pixie-Dingbats font are arms, legs, ...
    body = choice(("a","b","c","j","k","l","t","u"))
    face = choice(("d","e","f","m","n","o","v","w"))
    legs = choice(("g","h","i","p","q","r","x","y"))
    balloons = choice(("s","z"))
    
    _ctx.fill(cc, mc, yc, kc+random(-0.2,0.2))
    
    #Draw a body.
    _ctx.rotate(random(-20,20))
    _ctx.skew(random(-20,20),random(-20,20))
    _ctx.font("Pixie-Dingbats", pt * random(0.8,1.4))
    _ctx.text(body, x, y)
    _ctx.reset()
    
    _ctx.fill(cc, mc, yc, kc+random(-0.2,0.2))
    
    #Draw a face.
    _ctx.rotate(random(-20,20))
    _ctx.skew(random(-20,20),random(-20,20))
    _ctx.font("Pixie-Dingbats", pt * random(0.8,1.4))
    _ctx.text(face, x, y)
    _ctx.reset()
    
    _ctx.fill(cc, mc, yc, kc+random(-0.2,0.2))
    
    #Draw legs.
    _ctx.rotate(random(-20,20))
    _ctx.font("Pixie-Dingbats", pt * random(0.9,1.5))
    _ctx.text(legs, x, y)
    _ctx.reset()
    
    if random(100)>90:
        
        _ctx.fill(cc, mc, yc, kc+random(-0.2,0.2))
        
        #Draw balloon text.
        if random(100)>90:
            _ctx.rotate(random(-20,20))
            _ctx.font("Pixie-Dingbats", pt * random(0.9,1.5))
            _ctx.text(balloons, x, y)
            _ctx.reset()
        
def line(x1, y1, x2, y2):
    
    """Draws a pixie line from coordinates (x1,y1) to (x2,y2)
    """
    
    _ctx.push()
    
    #Set color to pixiecolor(), varying the K value
    #to simulate pen pressure.
    _ctx.colormode(CMYK)
    cc, mc, yc, kc = COLOR
    _ctx.fill(cc, mc, yc, kc+random(-0.2,0.2))
    
    #Calculate the length of the line as c.
    from math import sqrt, pow, asin, degrees
    a = x2 - x1
    b = y2 - y1
    c = sqrt(pow(a,2) + pow(b,2))
    
    #Choose line glyphs, according to the size of c.
    #This ensures that lines of different lengths
    #have more or less a same thickness after scaling them.
    pt = 30
    _ctx.font("Pixie-Dingbats", pt)
    if c < 150:
        glyphs = ("S","T")
        glyphwidth = 1.5*pt
    elif c > 400:
        glyphs = ("U","V","W","X")
        glyphwidth = 10.0*pt
    else:
        glyphs = ("M", "N", "O")
        glyphwidth = 5.5*pt
    
    #Determine the line's angle.
    d = degrees(asin(b/(c+0.0001)))
    if x2<x1: d = 180 - d
    
    #Scale the glyph to the length of the line.
    _ctx.transform(CENTER)
    f = c/glyphwidth+0.0001
    _ctx.scale(f,f)
    
    #Rotate the glyph to the line's angle.
    _ctx.transform(CORNER)
    _ctx.translate(x1/f,y1/f)
    _ctx.rotate(-d)
    
    #Draw the line glyph.
    _ctx.text(choice(glyphs), 0, 0)
    
    _ctx.pop()
    
def node(x, y, d):
    
    """Draws a small pixie circle.
    
    This function is expected to work with line(),
    together creating a network of nodes.
    """
    
    _ctx.push()
    
    #Set color to pixiecolor(), varying the K value
    #to simulate pen pressure.
    _ctx.colormode(CMYK)
    cc, mc, yc, kc = COLOR
    _ctx.fill(cc, mc, yc, kc+random(-0.2,0.2))
    
    pt = 30
    _ctx.font("Pixie-Dingbats", pt)
    glyphs = ("P","Q","R")
    
    #Scale the glyph to diameter d.
    _ctx.transform(CENTER)
    f = d/(0.6*pt)
    _ctx.scale(f)
    
    for i in range(random(1,3)):
    
        #Draw the glyph, with its center roughly at (x,y).
        _ctx.text(choice(glyphs), x-pt/2, y+pt/4)
    
    _ctx.pop()
    
def tree(root, nodes, x, y, width, height, pt=20, max=10, grow=False, border=False):

    """Draws a tree network scheme.
    
    Draws a tree scheme exploding from a central root.
    The nodes list is expected to contain, for example:
    [ ("node1",["leaf1a","leaf1b"]), ("node2",["leaf2a"]) ].
    Branches connect the nodes, and each node has its
    leaves drawn around it.
    
    Nodes grow smaller and smaller if grow is True.
    
    Uses line() and node() as callback to draw the network.
    
    """

    _ctx.push()

    #The number of nodes to draw
    count = min(max, len(nodes))

    #Create a path on which nodes can
    #placed later on.
    path = [(x,y)]
    _ctx.beginpath(x,y)
    x0 = x
    y0 = y
    for i in range(count):
        
        xradius = width/count*(i+0.1)
        yradius = height/count*(i+0.1)
        
        #A random location.
        #These "grow" further and further away
        #from the centre
        
        #dx = x+random(-xradius,xradius)/2
        #dy = y+random(-yradius,yradius)/2
        dx = x + xradius * random(0.25,0.5) * choice((-1,1))
        dy = y + yradius * random(0.25,0.5) * choice((-1,1))
        
        line(x0, y0, dx, dy)
        path.append((dx,dy))
        
        x0 = dx
        y0 = dy
        
    for x in range(count):
        
        #Get coordinates on path.
        dx = path[x+1][0]
        dy = path[x+1][1]
        
        #For each node, get its leaves.
        nodename, leaves = nodes[x]
        
        #Draw the leaves of a node around an oval.
        #The maximum of leaves is limited,
        #if you draw more the tree starts to look very unhumanlike.
        #I don't think you would draw trees with, say ten or twenty
        #leaves by hand.
        limit = 3
        angle = 15
        for i in range(min(limit,len(leaves))):
            
            w = random(-width/16,width/16)
            h = random(-width/16,width/16)
            line(dx, dy, dx+w, dy+h)
            paragraph(leaves[i], dx+w-30, dy+h+pt/4, width/5, pt*0.65)
            
        
        #Draw the node oval.
        #Oval grow smaller and smaller if grow was set to True.
        if grow: size = 1.0 - 0.5 * x/count
        else: size = 1
        node(dx, dy, pt*size)
        
        #Draw the example text on the oval.
        #Delay the first node,
        #we'll put that one on top later.
        if random(100)>95: keywords(nodename, all=choice((True,False)))
        paragraph(nodename, dx+pt/3, dy-pt/3, width/2, pt)
    
    #Draw the first central example text.
    dx = path[0][0]
    dy = path[0][1]
    node(dx, dy, pt)
    paragraph(root, dx+pt/3, dy-pt/3, width/2)
    
    #Draw a border around the diagram:
    if border:
        dx -= width/2
        dy -= height/2
        line(dx-pt/2, dy, dx+width-pt/2, dy)
        line(dx+width, dy-pt/2, dx+width-random(pt), dy+height-pt/2)
        line(dx+width, dy+height, dx, dy+height-random(pt))
        line(dx, dy+height, dx, dy)
        
    _ctx.pop()
    
def tornado(str, x, y):
    
    """Experimental tornade-style pixie text.
    
    Text that whirls around like a gust of wind.
    Provided as-is for now.
    
    """

    from math import sin, cos, tan, log10

    cX = random(1,10)
    cY = random(1,10)
    
    for i in range(len(str)):
        s = cos(cX)*20
        x += cos(cY)*s*1.2
        y += log10(cX)*1.2 + sin(cX) * 8
        _ctx.push()
        paragraph(str[i], x-s/2, y-s/2, 100, pt=max(15,abs(s*1.5)))
        _ctx.pop()
        cX += random(0.45)
        cY += random(0.15)