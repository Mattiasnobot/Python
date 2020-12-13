#Mattias Rannamäe IT-20
#harjutus 4
import random

#ruutude ja kuupide tabel
for i in range(1-11):
print("Arv   Ruut   Kuup")
arv = i
ruut = i*i
kuup = i*i*i






#Pank
print("***********************************************")
print("****************MNPANK*************************")
print("*****************€€€€€€€***********************")
print("***********************************************")
konto = 10000
intress = 0.05
aastad = 5

print("Aasta  Algsumma   Intress   Kokku")
#intressi arvutamine
for i in range(aastad):
    alg = konto
    konto = round(konto+(konto*intress),2)
    
    print(f"{i+1}  {alg:8} {intress*alg:.2f} {konto:8}")



input()


"""
#arvamismäng
print("***********************************************")
print("****************ARVAMISMÄNG********************")
print("******************only 2.99€*******************")
print("***********************************************")

arvamised = 0
kordade_arv = 3
suvaaarv = random.randint(1,6)

while arvamised<kordade_arv:
arvamised= arvamised + 1
arv = int(input("arva ära number vahemikus 1-5"))
if arv ==suvarv:
    print ("win")
    arvamised = 100
    else:
    print("Try again")
    if arvamised == kordade_arv:
        print("Lose")
        print("Game Over")
        
print(Mäng)

input()



#viisikud
for i in range(1,101):
if i%5==0:
print(i)


#korrutustabel

for i in range(1,11):
print(f"5 x{i} = {5*i}")



#Paaris ja paaritu

for i 
    kui on "paaris":
    print nr + paaris
else
    print nr + paaritu


#loto
print("tänased loto numbrid on:", end=" ")
for i in range(5):
    suvaarv = random.randint(0,9)
    print(suvaarv, end=" ")


#tärnid
#kahanev kolmnurk
maks = 6
for i in range(1,maks):
    print((maks-i)*"*")

#kasvav kolmnurk
for i in range(1,6):
    print("*"*i)



#tsykkel vahemikus 1-26
for i in range(1,26):
    #end määrab rea lõpu
    print("*", end=" ")
    #leiab 5ga jagunevad arvud
    jaak = i%5
    if jaak==0:
    #lisab reavahetused
  print(" ", end="\n")



#Jalgpall
vanus = int(input("sisesta vanus:"))
sugu = int(input("sisesta sugu:"))
if (vanus>=16 and vanus<=18):
    print("töötab")
else:
    print("ei tööta")





#müük
hind= int(input("Sisesta hind"))
if hind < 10:
    print ("hinda alantati 10%")
elif hind > 10:
    print("hinda alandati 20%")

#Juubel
synniaasta = int(input("Sünniaasta"))
vanus = 2020 -synniaasta
jaak = vanus%5
if jaak==0:
        print("Sul on see aasta juubel")
else:
        print("pole juubel")




#matemaatika
nr1 = int(input("sisesta nr1"))
nr2 = int(input("sisesta nr2"))
tehe = input("vali tehtemärk + - * /")
if tehe == "+":
    v=nr1+nr2
elif tehe == "-":
    v=nr1-nr2
elif tehe == "*":
    v=nr1*nr2
elif tehe == "/":
    v=nr1/nr2
    """