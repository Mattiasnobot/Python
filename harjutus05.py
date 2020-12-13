#Mattias Rannamäe IT-20
#25.11.2020
#harjutus 5


# Loendid

nimed = []


for i in range(5):
#küsib nime
nimi = input("Sisesta nimi:")
#lisab nime loendisse
nimed.append(nimi)
#näitab lisatud nime
print(nimi)
#Sorteerib nimed kasvavas järjekorras
nimed.sort()
print (nimed)