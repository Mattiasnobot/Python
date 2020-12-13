#Mattias Rannamäe IT-20
#02.12.2020
#harjutus06


#faili avamine
minu_fail = open('s6pru_l6ustaraamatus.txt', 'r')

#faili sisu kuvamine
ref = 0
kesk = 0
erakondi_kokku=[]
faili_sisu = minu_fail.readlines()
#faili sisu kuvamine
for i in range(len(faili_sisu)):
    enimi, pnimi, ek, sobrad = faili_sisu[i].split(" ")
    if ek=="RE":
        ref+=1
    elif ek=="KE":
        kesk+=1
    if ek not in erakondi_kokku:
        erakondi_kokku.append(ek)
    print(f"{enimi:11}{pnimi:10}{ek:4}{sobrad:5}", end="")
    
    #lisame andmed uude faili
    with open('poliitikud.txt','a') as fail_kirjutamiseks:
        fail_kirjutamiseks.write(enimi+" "+pnimi+"\h")
    
print("----------------\nReformikaid kokku: {ref}")
print(f"Kesikuid kokku: {kesk}")
print(f"erakondi kokku: {len(erakondi_kokku)}")

#faili sulgemine
minu_fail.close