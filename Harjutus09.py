#Mattias Rannamäe IT-20
#09.12.2020
#Harjutus09

ik = input("lisa isikukood: ")

if len(ik) == 11:
    p = ik[5:7]
    k = ik[3:5]
    a = ik[1:3]
    print(f"{p}.{k}.{a}")
    
