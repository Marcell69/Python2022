import random
import math

l=[]
for i in range(10):
    szam= random.random()
    l.append(math.floor(szam*90)+10)

print(l)

l=[]
for i in range(10) :
    l.append(random.randint(10,99))

print(i)

print (random.randint(-1000,1000*3))
l=[]
for i in range(100) :
    l.append(random.randint(-1000,1000*3))

print(l)

print(sum(l))
l5=[]
for e in l:
        if e%5==0:
                l5.append(e)

print(l5)

l5=[e//15 for e in l if e%5==0]

print(l5)

167
166
print(random.randrange(167,1667,2)*6)

print((random.randint(83,832)*2+1))

szavak=["alma","kürte","balack","banón","dinne","szőló"]
print( szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))
print("-"*20)
for e in szavak:
    print(e)
    kislista=[]
    kislista.append(e)
    kislista.append(random.randint(12,312))
    print(kislista)
    nagylista.append(kislista)

    print(nagylista)

for e in nagylista:
    print(e[0].ljust(10), 
                  str(e[1]).rjust(4),"kg","*"*(e[1]//6))

minimumErtek=int(input("Add meg, hogy hol kezdödjön:  "))
maxiumumErtek=int(input("Add meg, hogy hol kezdödjön:  "))
darab=("Mennyi darab kell:  ")

lista=[]

for i in range(darab):
        lista.append(random.randint(minimumErtek,maximumErtek))

print(lista)

legnagyobb=max(lista)
egyseg=80//legnagyobb

for e in lista:

    print(e)

#3jegyu szam bekeres

szam=int(input("Kérek egy 3 jegyű számot:    "))

print(szam)


















