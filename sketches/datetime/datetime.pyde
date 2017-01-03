import datetime as dt

def setup():
    size(640, 480)
    font = createFont("Coda-Heavy.ttf", 96)
    textFont(font)

def draw():
    background("#000000")
    myNow = dt.datetime.now()
    myHour = str(myNow.hour)
    myMinute = myNow.minute
    if myMinute < 10:
        myMinute = "0" + str(myMinute)
    else:
        myMinute = str(myMinute)
    mySecond = myNow.second
    if mySecond < 10:
        mySecond = "0" + str(mySecond)
    else:
        mySecond = str(mySecond)
    myTime = myHour + " : " + myMinute + " : " + mySecond
    textSize(96)
    text(myTime, 60, 150)
    rente = dt.date(2018, 12, 31)
    heute = dt.date.today()
    differenz = rente - heute
    myDays = str(differenz.days)
    workingDays = round(float(myDays)/7.0, 0) * 5
    workingDays = str(int(workingDays - 80))
    myText = u"Lieber Jörg, es sind nur noch " + myDays + \
    u" Tage bis zur Rente!\n Das sind etwa " + \
    workingDays + " Arbeits- tage. Das schaffst Du!"
    textSize(32)
    text(myText, 60, 200, 540, 300)
 