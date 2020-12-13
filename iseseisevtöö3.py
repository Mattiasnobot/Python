#Mattias Rannamäe IT-20
#ryhm 1
#is.ülesanne 3
import random

#Jukebox





#Sissetulek
fail = open("konto.txt")
for i in fail:
    if float(i) >0:
    print(i,end=" ")

#Jänesevanemate mure ver.3
ringide_arv = abs(int(input("Ringide arv: ")))
porgandite_arv = 0
for i in range(1,ringide_arv+1):
    if i %2 ==0:
        porgandite_arv = porgandite_arv + i
print(f"saadavate porgandite koguarv on {porgandite_arv}.")

#Ülikooli vastuvõetud
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()
aasta = int(input("Sisesta aasta 2011;2019: "))
print(f"{aasta}. aastal oli vastuvõetud {vastuvõetud[aasta-2011]}")