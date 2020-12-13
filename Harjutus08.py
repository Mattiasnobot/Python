#Mattias Rannamäe IT-20
#09.12.2020
#Harjutus08

class Auto:
    #adribuudid
    mark = ""
    aasta = 0
    hind = 0
    varv  = "värv lisamata"
    maxkiirus= 280

    #meetodid
    def __init__(self,x,y,z, i, j):
        self.mark = x
        self.aasta = y
        self.hind = z
        self.varv = i
        self.maxkiirus = j
        
    def lisamark(self,x):
        self.mark = x
        
    def lisaaasta(self,y):
        self.aasta = y
    
    def lisahind(self,z):
        self.hind = z
        
    def lisavärv(self,i):
         self.varv = i
         
    def lisamaxkiirus(self, j):
         self.maxkiirus = j
        
    def kuva(self):
        print(f"Mark: {self.mark}\nAasta: {self.aasta}\nHind: {self.hind}")
        print(f"värv: {self.varv}\nMaxkiirus: {self.maxkiirus}")
        
minuAuto = Auto("BMW", 1990, 1000, "hall", 280)
minuAuto.kuva()