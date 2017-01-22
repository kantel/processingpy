# Der Lorenz-Attraktor, eine Ikone der Chaos-Theorie

Nachdem ich im letzten Abschnitt die Schmetterlingskurve mit Processing.py gezeichnet hatte, wollte ich nun darauf aufbauen und eine Ikone der Chaos-Forschung, den [Lorenz-Attraktor][3] damit zeichnen. Ich hatte das ja auch schon einmal [mit R getan][4] -- dort findet Ihr auch weitere Hintergrundinformationen zu diesem Attraktor --, aber mit R wurde nur das fertige Ergebnis visualisiert. Hier kommt es mir aber wieder darauf an, die Entstehung der Kurve verfolgen zu können und dafür ist, wie schon bei der Schmetterlingskurve, Processing gut geeignet:

[![Screenshot](images/lorenzprocessingpy.jpg)](https://www.flickr.com/photos/schockwellenreiter/32063849580/)

Als einer der ersten hatte  1961 [Edward N. Lorenz](http://de.wikipedia.org/wiki/Edward%20N.%20Lorenz), ein Meteorologe am [Massachusetts Institute of Technology](http://de.wikipedia.org/wiki/Massachusetts%20Institute%20of%20Technology) (MIT), erkannt, daß Iteration Chaos erzeugt. Er benutzte dort einen Computer, um ein einfaches nichtlineares Gleichungssystem zu lösen, das ein simples Modell der Luftströmungen in der Erdatmosphäre simulieren sollte. Dazu benutzte er ein System von sieben Differentialgleichungen, das [Barry Saltzman](http://www.yale.edu/opa/arc-ybc/v29.n18/story18.html) im gleichen Jahr aus den [Navier-Stokes-Gleichungen](http://de.wikipedia.org/wiki/Navier-Stokes-Gleichungen) [^1] hergeleitet hatte. Für dieses System existierte keine analytische Lösung, also mußte es numerisch (d.h. wie damals und auch heute noch vielfach üblich in FORTRAN) gelöst werden. Lorenz hatte entdeckt, daß bei nichtperiodischen Lösungen der Gleichungen vier der sieben Variablen gegen Null strebten. Daher konnte er das System auf drei Gleichungen reduzieren:

[^1]: Eine sehr schöne Einführung in [das ungelöste Problem der Navier-Stokes-Gleichungen][5] gibt es von *Florian Freistetter* in der 217. Folge seiner *Sternengeschichten*

$$
\begin{align}
\frac{dx}{dt} & = -\sigma (y - z) \\\\
\frac{dy}{dt} & = (\rho - z)x - y \\\\
\frac{dz}{dt} & = xy - \gamma z
\end{align}
$$

Dabei sind \\(\sigma = -10\\), \\(\rho = 40\\) und \\(\gamma = - \frac{8}{3}\\). Die Parameter der Gleichung habe ich *[Herm1994]* entnommen, *[Stew1993]* gibt \\(\rho = 28\\) an, aber der Wert ändert nichts an dem Verhalten der Kurve und \\(\rho = 40\\) füllt das Fenster einfach besser aus. 😜

Processing.py besitzt im Gegensatz zu R oder [NumPy][7] kein Modul zur numerischen Lösung von Differentialgleichungen und so habe ich das einfache [Eulersche Poligonzugverfahren][6] zur numerischen Berechnung benutzt

~~~python
    dx = -sigma*(x - y)*dt
    dy = (x*(r - z) - y)*dt
    dz = (x*y - b*z)*dt
    x += dx
    y += dy
    z += dz
~~~

und dabei konstant `dt = 0.01` gesetzt. Das benötigt natürlich mehr Rechenkapazität, als sie Lorenz je zur Verfügung standen, aber trotz der größeren Genauigkeit ändert sich nichts am chaotischen Verhalten der Kurve. Für die Farbberechnugn habe ich dieses mal nur den Farbwert (*Hue*) bei jeder Iteration geändert, Sättigung (*Saturation*) und Helligkeit (*Brightness*) bleiben konstant auf dem höchsten Wert. Das ergibt kräftige Farben, die von Rot über Orange nach Gelb und dann nach Grün, Blau und Violett wandern. So kann man schön erkennen, daß die beiden »Flügel« des Attraktors immer wieder, aber für uns unvorhersehbar, durchlaufen werden.

## Der Quellcode

Hier nun der vollständige Quellcode des Skripts. Er ist kurz und selbsterklärend und folgt weitestgehend dem Pascal-Programm aus *[Herm1994]*, Seiten 80ff.

~~~python
b = 8.0/3
r = 40.0
sigma = 10.0
dt = 0.01
x = y = 0.01
z = t = 0.0
xOld = zOld = 0.0
first = True

def setup():
    size(640, 480)
    background(0)
    colorMode(HSB, 100)

def draw():
    global x, y, z, t, xOld, zOld
    global first
    strokeWeight(1)
    stroke(t, 100, 100)
    dx = -sigma*(x - y)*dt
    dy = (x*(r - z) - y)*dt
    dz = (x*y - b*z)*dt
    x += dx
    y += dy
    z += dz
    # auf Fenstergröße skalieren
    xx = (x*8) + 320
    zz = 470 - (z*5.5)
    if first:
        point(xx, zz)
    else:
       line(xOld, zOld, xx, zz)
    xOld = xx
    zOld = zz
    first = False 
    t = t + dt
    if ( t >= 75.0):
       print("I did it, Babe!")
       noLoop()
~~~

## Links

  * Der *[Lorenz Attractor](http://mathworld.wolfram.com/LorenzAttractor.html)* auf Wolfram MathWorld

<div style="float: right; margin-left: 12px; margin-top: 6px;"><iframe src="http://rcm-de.amazon.de/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=derschockwell-21&o=3&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=345833243X" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>&nbsp;<iframe src="http://rcm-de.amazon.de/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=derschockwell-21&o=3&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=3893196331" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe></div>

## Literatur

  * *[Herm1994]* Dieter Hermann: *<a href="http://www.amazon.de/gp/product/3893196331/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=3893196331&linkCode=as2&tag=derschockwell-21">Algorithmen für Chaos und Fraktale</a><img src="http://www.assoc-amazon.de/e/ir?t=derschockwell-21&l=as2&o=3&a=3893196331" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />*, Bonn (Addison-Wesley) 1994, S. 80ff.
  * *[Pief1991]* Frank Piefke: *<a href="http://www.amazon.de/gp/product/3778519158/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=3778519158&linkCode=as2&tag=derschockwell-21">Simulationen mit dem Personalcomputer</a><img src="http://www.assoc-amazon.de/e/ir?t=derschockwell-21&l=as2&o=3&a=3778519158" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />*, Heidelberg (Hüthig) 1991
  * *[Stew1993]* Ian Stewart: *<a href="http://www.amazon.de/gp/product/345833243X/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=345833243X&linkCode=as2&tag=derschockwell-21">Spielt Gott Roulette?</a><img src="http://www.assoc-amazon.de/e/ir?t=derschockwell-21&l=as2&o=3&a=345833243X" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />*, Frankfurt (Insel TB) 1993

[3]: https://de.wikipedia.org/wiki/Lorenz-Attraktor
[4]: http://blog.schockwellenreiter.de/essays/lorenzr.html
[5]:  http://scienceblogs.de/astrodicticum-simplex/2017/01/20/sternengeschichten-folge-217-das-ungeloeste-problem-der-navier-stokes-gleichungen/
[6]: https://de.wikipedia.org/wiki/Explizites_Euler-Verfahren
[7]: http://cognitiones.kantel-chaos-team.de/programmierung/python/numpy.html