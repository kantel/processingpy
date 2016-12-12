from time import *

letzterArbeitstag = "2016-12-31"
rente = mktime(letzterArbeitstag)
println(rente)

lt = localtime()
println(lt)

diff = rente - lt
print(diff)