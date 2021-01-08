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

nimi = ""
sleep = 2
#Pahalased
#ORK
def ork():
    elud = 5
    tugevus = print(random.randrange(2,5))
    kaitse = print(random.randrange(1,2))
    level = 1
    
#Kobold (väike traakon)
def kobold():
    elud = 10
    tugevus = print(random.randrange(4,7))
    kaitse = print(radom.randrange(5,8))
    level = 2
    
    #story
def prolog():
    print("Mangu algus")
    time.sleep(sleep)
    print("Olid sopradega eelmine ohtu kortsis")
    time.sleep(sleep)
    print("Hommikul aga arkasid paksus metsas mida sa ei teadnud")
    time.sleep(sleep)
    print("Sa tunnetad kergeid maa varinaid ja vaatad ringi ning markad, et ork on sinu poole teel")
    time.sleep(sleep)
    print("Sa üritad mõõka haarata aga see on kusagile kadunud.")
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
    print ("\nSa jäid ootele. Särisev mõõk tõmbas ligi "
    "ork, kes arvas, et sa pole matš. Kui ta kõndis"
    "lähemale ja lähemale, teie süda tuksus kiiresti. Orkina"
    "sirutas käe, et mõõk haarata, torkasite tera sisse"
    "selle rind. \n\nSa jäid ellu!")
   else: #kui mangija ei votaks mooka
     print ("\nTe oleksite pidanud selle mõõga kätte võtma. Sa oled "
     "kaitsetu. \n\nSa said surma!")
  elif otsus in Vastus_C:
    print ("Kui ork siseneb pimedasse koopasse, teete kavalalt "
    "hiilige välja. Olete mitme jala kaugusel, kuid ork pöördub"
    "ringi ja näeb sind jooksmas.")
    valik_jookse()
  else:
    valik_koobas()

def valik_jookse():
  print ("\nJooksete nii kiiresti kui võimalik, kuid ork "
  "kiirus on liiga suur. Kas sa:")
  time.sleep(1)
  print ("""  A. Peida rahnu taha
  B. Oled lõksus ja võitled end välja
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
  "mudas lebav mõõk. Sa jõuad kiiresti alla ja haarad selle kinni,"
  "aga jäta vahele. Proovid varjata oma rasket hingamist."
  "mahajäetud hoone taga, oodates orki tulekut"
  "laaditakse nurga taga. Märkate lillat õit"
  "jala lähedal. Kas sa võtad selle üles? Y/N")
  otsus = input(">>> ")
  if otsus in jah:
    lill = 1 #lisab lille inventori
  else:
    lill = 0
  print ("Kuulete selle raskeid samme ja olete valmis selleks "
  "eelseisev ork.")
  time.sleep(1)
  if lill > 0:
    print ("\Sirutate kuidagi lillaka õie välja "
    "Loodan, et see peatab orki. See teeb! Ork otsis"
    "armastuse pärast. "
    "\n\nSee muutus imelikuks aga sa jäid elama!")
  else: #kui mangija ei votaks mooka
     print ("\nVõib-olla oleksite pidanud lille üles võtma. "
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
                #"Tase": tase
                #"Tugevus": tugevus
                #"Kaitse": kaitse
                } 


    f = open(nimi+".txt", "w")
    f.write (str(mangijal))
    f.close()
    

    
#tööle panemine
loop = 1
while loop == 1:
    Mangija()
    
    prolog()
    

print("game over")

    