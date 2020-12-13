# Mattias Rannamäe IT-20
# 19.11.2020
# ülesanne 02
import math


#ajateisendus





#hüpotenuus
a,b = 16,9
c= math.sqrt(a**2+ b**2)
print("kolmnurga hüpotenuus on",c)


#Rulluisutajad
kiirus = 29.9
aeg = 24/60
dist = kiirus*aeg
print("distantsi pikkus on:",dist"km kaugusel")


#hind
hind = 12.90
kogus = 3
tip = 1.1


Summa = (hind*tip)/kogus
print("Iga üks peab maksma:",Summa)


#tootehind
hind = 36.75
ale = 0.4
kogus = 3

Summa = (hind-(hind*ale))*kogus
print("Kolme toote summa:",Summa)


#kolmnurga ümbermõõt
a = 2
b = 3
c = 4
P = a+b+c
print("kolmnurga P = :",P)