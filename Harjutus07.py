#Mattias Rannamäe IT-20
#02.12.2020
#harjutus 07

#Ruum alade mäng






def minuApp():
    print("*************Ruumala leidmine V1*****************")
    print("Vali kujund\n1 Kuup\n2 Kera\n3 Koonus\n4 Silinder\n0 Sulge programm")
    print("*************************************************")
    valik = int(input("Sisesta soovitud kujundi number: "))
    if valik==1:
        print(f"kuubi pindala on {kuup()}")
    elif valik==2:
        print(f"kuubi pindala on {kera()}")
    elif valik==3:
        print(f"kuubi pindala on {koonus()}")
    elif valik==4:
        print(f"kuubi pindala on {silinder()}")
    elif valik>4:
        print("Sellist valikut pole!")
    else:
        return valik
    
def kuup():
    print("Leian kuubi")
    x=int(input("Sisesta külg 1: "))
    y=int(input("Sisesta külg 2: "))
    z=int(input("Sisesta külg 3: "))
    v= x*y*z
    return v
    
    
def kera():
    print("Leian kera")
    r= int(input("Sisesta kera raadius: "))
    v=round(4/3*3.14*pow(r,3),2)
    return v

def koonus():
    print("Leian koonus")
    
def silinder():
    print("Leian Silinder")

#käivitab minu programmi 
loop = 1
while loop==1:
   v= minuApp()
    if v==0:
        loop=0
        
print ("Programmi lõpp")




#funktsiooni loomine
def Tervita(keel="ge"):
    'Tervitab keele järgi'
    if keel=="et":
        nimi = input("sisesta oma nimi: ")
        return "Tere "+nimi+"!"
    elif keel=="en":
        nimi= input("Enter your name: ")
        return "Hi "+nimi+"!"
    elif keel=="ge":
        nimi=input("gib deinen Namen: ")
        return "Hallo"+nimi+"!"

print(Tervita(et))

