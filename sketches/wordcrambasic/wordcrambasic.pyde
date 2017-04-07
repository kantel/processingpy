add_library('WordCram')

def setup():
    size(700, 400)
    background(255)
    
    wordcram = WordCram(this
        ).fromWebPage("http://blog.schockwellenreiter.de/2017/04/2017040404.html"
        ).sizedByWeight(0, 150
        ).withFont("Copse"
        )
    wordcram.drawAll()