# Eine analoge Uhr aus Kreisbögen

In seiner 74. Coding-Challenge auf YouTube zeigte *Daniel Shiffman*, wie man mit P5.js, dem JavaScript-Mode von Processing eine analoge Uhr aus Kreisbögen programmiert. Inspiriert wurde er von *John Maedas* [12 o'Clocks](http://cmuems.com/2016/60212/lectures/lecture-09-09b-clocks/maedas-clocks/)-Projekt und ich unterlag der Versuchung, *Shiffmans* JavaScript-Programm nach Processing.py zu portieren:

[![Screenshot clock.py](images/clockpy.jpg)](https://www.flickr.com/photos/schockwellenreiter/37277064432/)

Dabei habe ich gegenüber dem Original-Script nur einige kleine Veränderungen vorgenommen.Ich habe die Stunden in den äußeren Kreisbogen gelegt und dadurch die Sekunden in den inneren Kreisbogen. Und ich habe die Zeiger der Uhr nicht nur in unterschiedlichen Längen, sondern auch in unterschiedliche Dicken zeichnen lassen, wie man es von analogen Uhren gewohnt ist. Außertdem habe ich heftigen Gebrauch vom `with`-Statement gemacht, das in Processing.py in vielen Fällen nicht nur das `push` und `pop` ersetzen, sondern auch ungterschiedliche Statii klasmmern kann.

## Der Quellcode

Meiner Meinung nach ist der Quellcode gegenüber der JavaScript-Version übersichtlicher geworden und leichter zu durchschauen. Das liegt aber sicher nicht an meinen genialen Programmierkenntnissen (die sind eher bescheiden), sondern ist der Klarheit von Python geschuldet:

~~~python
baseStroke = 8

def setup():
    size(400, 400)
    frameRate(30)
    
def draw():
    background(0)
    translate(width/2, height/2)
    rotate(radians(-90))
    
    hr = hour()
    mn = minute()
    sc = second()
    
    secondAngle = map(sc, 0, 60, 0, 360)
    minuteAngle = map(mn, 0, 60, 0, 360)
    hourAngle = map(hr%12, 0, 12, 0, 360)
    noFill()
    strokeWeight(baseStroke)
    
    # Kreisbögen
    with pushStyle(): # Sekunden
        stroke(150, 100, 255)
        arc(0, 0, 300, 300, radians(0), radians(secondAngle))
    with pushStyle(): # Minuten
        stroke(255, 100, 150)
        arc(0, 0, 320, 320, radians(0), radians(minuteAngle))
    with pushStyle(): # Stunden
        stroke(150, 255, 100)
        arc(0, 0, 340, 340, radians(0), radians(hourAngle))

    # Zeiger
    with pushMatrix(): # Sekunden
        strokeWeight(baseStroke/4)
        stroke(150, 100, 255)
        rotate(radians(secondAngle))
        line(0, 0, 100, 0)
    with pushMatrix(): # Minuten
        strokeWeight(baseStroke/2)
        stroke(255, 100, 150)
        rotate(radians(minuteAngle))
        line(0, 0, 80, 0)
    with pushMatrix(): # Stunden
        strokeWeight(baseStroke)
        stroke(150, 255, 100)
        rotate(radians(hourAngle))
        line(0, 0, 60, 0)

    noStroke()
    fill(255, 255, 255)
    ellipse(0, 0, 10, 10)
~~~

## Shiffmans Coding Challenge

Zur Information hier auch noch Shiffmans *Coding Challenge*, damit Ihr die Implementierungen vergleichen könnt:

<iframe width="560" height="315" src="https://www.youtube.com/embed/E4RyStef-gY" frameborder="0" allowfullscreen></iframe>

## Links

- *Golan Levins* [Notizen](http://cmuems.com/2016/60212/lectures/lecture-09-09b-clocks/maedas-clocks/) zu Maedas 12 o’Clocks nebst [Anhang](http://cmuems.com/2016/60212/lectures/lecture-09-09b-clocks/)
- [Alca's Clock Collection](https://codepen.io/collection/DqRNLQ/) auf CodePen