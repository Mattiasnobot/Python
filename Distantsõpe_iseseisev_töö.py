#Mattias Rannamäe IT-20
#14.12.2020
#Iseseisvad ülessanded

#Ülessanne 4
#Eesti lipp
for i in range(1,5):
    print('\n')
    for j in range(1,70+1):       
        print('¤', end='')

for i in range(1,4):
    print('\n')
    for j in range(1,70+1):      
        print('=', end='')

for i in range(1,4):
    print('\n')
    for j in range(1,70+1):     
        print('-', end='')

print("\n")
print("\n")
print("\n")
print("\n")

#Ülessanne 12

#kolmnurk
print("*\n"
      "***\n"
      "*****\n"
      "***\n"
      "*\n")


#kahanev kolmnurk
maks = 6
for i in range(1,maks):
    print((maks-i)*"*")
    
print("---------\n")
#kasvav kolmnurk
for i in range(1,maks):
    print("*"*i)
print("---------\n")

#Peegel kolmnurk
maks = 6
for i in range(1,maks):
    print((maks-i)*"*")
for i in range(1,maks):
    print("*"*i)



#Ülessanne 8
#tagurpidi lause
laused = input("Sisesta lause:")
laused = laused.split()
laused = list(reversed(laused))
print(" ".join(laused))

print("---------\n")

#Ülessanne 9
#nr 1-66
for i in range(1,66+1):
    print(i,end=" ")

print("\n")



#Ülessanne 1
#liitmine
arv1 = int(input("Sisesta esimene arv mida soovid liita: "))
arv2 = int(input("Sisesta teine arv mida soovid liita: "))
liitmine = arv1 + arv2
print(liitmine)
