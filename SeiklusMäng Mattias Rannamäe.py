#Mattias Rannamäe
#IT-20
import random
import time
from pathlib import Path
import os



#Vastuse varjandid
Vastus_A = ["A", "a"]
Vastus_B = ["B", "b"]
Vastus_C = ["C", "c"]
jah = ["Y", "y", "jah"]
ei = ["N", "n", "ei"]

mookdmg = random.randint(4,8)
elud= 20
ork_elud=5
dmg=6
alive= 1
tase = 1
mookdmg=3
ork_dmg= random.randint(2,5)



#Pahalased
#ORK

def ork():
    ork_elud = 5
    tugevus = print(random.randrange(2,5))
    kaitse = print(random.randrange(1,2))
    level = 1
    
    #story
def prolog():
    print("Mangu algus")
    time.sleep(sleep)
    print("Olid sopradega eelmine ohtu kõrtsis")
    time.sleep(sleep)
    print("Hommikul aga arkasid paksus metsas mida sa ei tundnud")
    time.sleep(sleep)
    print("Sa tunnetad kergeid maa varinaid ja vaatad ringi ning märkad, et ork on sinu poole teel")
    time.sleep(sleep)
    print("Sa üritad mõõgast haarata aga see on kusagile kadunud.")
    time.sleep(sleep)
    print("""  A. Võtad maast kivi ja viskad orki
  B. Viskad pikali ja ootad kuniks ta sust üle jookseb
  C. Jooksed nii kiirelt kui saad""")
    
    otsus = input("Mida sa teed?")
    if otsus in Vastus_A:
        valik_kivi()
    elif otsus in Vastus_B:
        print ("\nSee käis kiiresti. "
        "\n\nSa said surma!")
    elif otsus in Vastus_C:
        valik_jookse()
        
def valik_kivi():   
    print ("Ork jäi paigale, kuid toibus. Ta hakkab "
    "sinu poole jooksma jälle. Kas sa:")
    time.sleep(1)
    print ("""  A. Jooksed
    B. Viskad teise kivi
    C. Jooksed lähedal olevasse koopasse""")
    otsus = input(">>> ")
    if otsus in Vastus_A:
        valik_jookse()
    elif otsus in Vastus_B:
        print ("Otsustasite visata veel ühe kivi, täpselt nagu  esimese " 
        "visatud kivi tegi palju kahju. Kivi lendas üle "
        "orki pea. viskaisd mööda. \n\nSa said surma!")
    elif otsus in Vastus_C:
        valik_koobas()
    
def valik_koobas():
  print ("\nSa kõhklesid, kuna koobas oli pime ja "
  "rõske. Enne täielikku sisenemist märkate maas säravat mõõka. "
  "Kas sa võtad mõõga kätte. Y/N?")
  otsus = input(">>> ")
if otsus in jah:
        mook = 1 #lisab mõõga mida saab kasutada
else:
    mook = 0
    print ("\nMida sa teed järgmiseks?")
    time.sleep(1)
    print ("""  A. Peitud ja oled vaikselt
    B. Võitled
    C. Jooksed""")
    otsus = input(">>> ")
    if otsus in Vastus_A:
        print ("\nKas tõesti? Peidete end pimedasse? Ma mõtlen "
        "orkid näevad pimedas väga hästi, eks? Kas pole kindel, aga"
        "Ma lähen koos jahiga, nii...\n\nSa said surma!")
    elif otsus in Vastus_B:
        if mook > 0:
            print ("\nSa olid paigal ja nägid säravat mõõka ja otsustasid sellest haarata. "
                   "\nTe hakkasite võitlema")
#Võitlus                   
while alive == 1:
    while ork_elud>=0 and elud>=0:
        ehit = random.randint(1,1)
        if ehit == 1:    
            ork_elud= ork_elud-(mookdmg*dmg)
            mhit = random.randint(1,3)
        if mhit == 2:
            elud = elud-(ork_dmg*mhit)
                              
        if elud>ork_elud:
            print("sa jäid elama")
            print(f"V:{ork_elud}")
            print(f"M:{elud}") 
            tase+=1
            print(f"level: {tase}")
        else:
            print("kaotus")
            print(f"level: {tase}")
                                    
        if alive == 0:
            print("Mäng läbi!")
        else: #kui mangija ei votaks mooka
            print ("\nTe oleksite pidanud selle mõõga kätte võtma. Sa oled "
                     "kaitsetu. \nSa said surma!")
        elif otsus in Vastus_C:
            print ("Kui ork siseneb pimedasse koopasse, teete kavala liigutuse "
                    "ja hiilite välja. Olete orkist päris kaugel, kuid ork pöörab"
                    "ringi ja näeb sind jooksmas.")
            valik_jookse()
        else:
            valik_koobas()

def valik_jookse():
  print ("\nJooksete nii kiiresti kui võimalik, kuid orki "
  "kiirus on liiga suur. Kas sa:")
  time.sleep(1)
  print ("""  A. Peidad rahnu taha
  B. Oled nurgas ja võitled end välja
  C. Jookse mahajäetud linna poole""")
  otsus = input(">>> ")
  if otsus in Vastus_A:
    print ("Sa oled kergesti märgatav. "
    "\n\nSa said surma!")
  elif otsus in Vastus_B:
    print ("\nSa oled jõuetu orki vastu. "
    "\n\nSa said surma!")
  elif otsus in Vastus_C:
    valik_linn()
  else:
    valik_jookse()
    
def valik_linn():
  print ("\nMeeletult joostes märkate roostetanud "
  "mudas lebavat mõõk. Sa jooksed kiiresti mõõga poole ja haarad sellest,"
  "aga jätsid selle maha. Proovid vaigistada oma rasket hingamist."
  "mahajäetud hoone taga, oodates orki tulekut"
  "peitud nurga taga. Märkate lillat õit"
  "jala lähedal. Kas sa võtad selle üles? Y/N")
  otsus = input(">>> ")
  if otsus in jah:
    lill = 1 #lisab lille inventori
  else:
    lill = 0
    print("Kuulete orki raskeid samme ja olete valmis selleks "
  "eelseisev ork.")
  time.sleep(1)
  if lill > 0:
    print("\Sirutate käega lillaka õie välja "
    "Loodan, et see peatab orki. Ork peatus"
    "ilusa lille pärast. "
    "\nSee muutus imelikuks aga sa jäid elama!")
  else: #kui mangija ei votaks mooka
     print("\nVõib-olla oleksite pidanud lille üles võtma. "
     "\n\nSa said surma!")    


def Mangija():
    nimi = input("Sisesta mängija nimi: ")
    time.sleep(sleep)
    if Path(nimi+".txt").is_file():
        #endise mängija fail eksisteerib
        print("Mängija eksisteerib!")
        print("Kasutan eelnevailt olemasolevat Mängia", nimi, "andmeid.")
        print("\nTere tulemast, "+(nimi)+"!")
        print("Siin on teie skoor: ")
        #olemas olevad andmed
        ex = open(nimi+".txt", 'r').read()
        whip = eval(ex)
        return whip
    else:
        #Uue mangija tervitamine
        print("Uus kasutaja on loodud")
        time.sleep(sleep)
        nimi = nimi.capitalize()
        print("Tere tulemast "+(nimi)+"!")
        nimi
        tase = 1
        tugevus = 8
        kaitse = 4
        time.sleep(sleep)
        print("Teie hetke \ntase ", tase, "\ntugevus", tugevus,"\nkaitse ", kaitse)
        time.sleep(sleep)
        valik = str(input("Otsustage kuhu sooviksite oma 6 punkti juurde lisada [tugevus/kaitse]"))
        punktid = 6
        # punktide lisamine
        if valik == "tugevus":
            tugevus = 8
            tugevus = tugevus + punktid
            num = str(tugevus)
            num2 = str(kaitse)
            print("tugevus: "+num)
        else:
            kaitse = 4
            kaitse = kaitse + punktid
            tugevus = tugevus - 3
            print("tugevus: "+(num - 3))
            print("kaitse : "+(num2))
        
    time.sleep(sleep)
    print("mangija adribuudid [nimi].txt faili salvestamine")
    time.sleep(sleep)
    
    #mangija kasutaja salvestamine
    oskused = [nimi, tase, tugevus, kaitse]
    mangijal = {"Nimi": nimi
                "Tase": tase
                "Tugevus": tugevus
                "Kaitse": kaitse
                } 


    f = open(nimi+".txt", "w")
    f.write (str(mangijal))
    f.close()
    

    
#tööle panemine
loop = 1
while loop == 1:
    Mangija()
    
    prolog()
    

print("Mäng läbi!")

    