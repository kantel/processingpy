from WordCram import wordcram

def setup():
    size(700, 400)
    background(230)
    wordArray = [("Hello", 100), ("WordCram", 60)]
    
    wordcram = WordCram(this).fromWords(wordArray)
    wordcram.drawAll()