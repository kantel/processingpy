import datetime as dt

rente = dt.date(2018, 12, 31)
println(rente)
heute = dt.date.today()
println(heute)
differenz = rente - heute
println(differenz)
s = str(differenz)
println(s)
s = s[:3]
println(s)