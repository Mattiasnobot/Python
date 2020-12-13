#Mattias Rannamäe IT-20
#8.12.2020
#4.iseseisev töö

#Kuupäev

def kuu_nimi(kp):
    kuud = ('jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember');
    p, k, a = kp.split(" . ")
    kuup = kuud[int(k)-1]
    return kuup
    
def kuupäev_sõnena(kp):
    p, k, a = kp.split(" . ")
    kuunimi = kuu_nimi(kp)
    return p+"."+kuunimi+". a "


kuup = int(input("sisesa kuu päev kujul pp.kk.aaaa: "))

print(kuupäev_sõnena(kuup))



input()

#Mündid
myndid = []
fail = open ("mündid.txt")
for line in fail:
    myndid.append(int(line))

def pronksikarva_summa(myndid):
    konto = 0
    for i in myndid:
        if i =1 or i =2 or i =5:
            konto = konto + i
    print (f"hoiupõrsasse läheb {konto} senti.")       
pronksikarva_summa[myndid]
        

















#Tervitused mõtisklustega

def tervitus(arv):

arv = int(input("Sisestage külaliste arv: "))
for i in range(arv):
    print("Võõrustaja: \"Tere!\" \n Täna {i}. kord tervitada mõtiskleb võõrustaja \n Külaline: \"Tere, suur tänu kutse eest!\"")


#Peo eelarve

def eelarve(v, m):
    y= 4454
    x= 20
    return [y, x]

v = int(input("Mitu inimest on kutusutud"))
m = int(input("Mitu inimest tuleb?"))
list = eelarve(v, m)
print(f"Maksimaalne eelarve: {list[0]} €")
print(f"Miinimum eelarve: {list[1]} €")


#Õunamahla tegemine

def mahlapakkide_arv(kogus):
    mahlapakkidearv =round(kogus * 0.4/3,0)
    return int(mahlapakkidearv)
kogus = int(input("Sisestage õunte kogus kg: "))

print(mahlapakkide_arv(kogus))

#bänner

def banner(t):
    return t.upper()
korda = int(input("Mitu korda reklaamlauset kuvatakse:"))
b = input("Sisestage reklaamlause:")

for i in range(korda):
    print(banner(b))
