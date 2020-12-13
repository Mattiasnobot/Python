#ryhm 1
#is.ülesanded 1-2

#ounad
ounad = 14
poial


#taringud
import random
taringute_arv = int(input("Täringute arv: "))
for i in range (taringute_arv):
    print(random.randint(1,6))





#Murelikud lastevanem

ringide_arv = abs(int(input("Sisestage ringide arv: ")))
jaak = ring%2
porgandid = 0
ring = 1
while ringide_arv>=ring>0:
    if ring%2 ==0:
         porgandid+=ring
         
         ring+=1
    print(porgandid)
    
    
    
    
#äratus
korda = int(input("mitu korda kell heliseb: "))
for i in range(korda):
    print("Tõuse ja sära!")


#buss
inimeste_arv = int(input("Sisestage inimeste arv: "))
kohtade_arv = int(input("Sistage kohtade arv: "))
if inimeste_arv%kohtade_arv ==0:
    print(inimeste_arv//kohtade_arv)
else:
    print(inimeste_arv//kohtade_arv+1)
    print(f"viimases bussis on {inimeste_arv%kohtade_arv} inimest.")



#pilved
alus = float(input( "pilvede aluse kõrgus "))

if alus > 6:
    print("Need on ülemised pilved")
else:
    print("Need ei ole ülemised pilved")



#Aasta liblikas

aasta = 2020
libikas = "teelehemosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta)+lause_keskosa+liblikas
print(lause)

#tervitus
    print("tere, maailm!")