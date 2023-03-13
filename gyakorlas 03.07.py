def oszlopVissza(hanyadik):
    oszlop=[]
    for e in tabla:
        oszlop.append(e[hanyadik-1])

    return oszlop





gyumolcsok=["alma","szőlő","körte","barack","dragonfruit","licsi"]

print("Ennyi gyümölcs van: {}".format(len(gyumolcsok)))

print(gyumolcsok[3])
#gyumolcsok[3]+="k"
#gyumolcsok[3]="barack"

gyumolcsok.index("barack")
#gyumolcsok[gymolcsok.index("barack")+="k"
index=gyumolcsok.index("barack")
gyumolcsok[index]+="k"

print(gyumolcsok[3])

print("rövid gyümölcsök")
#for i in range(len(gyumolcsok)):
#   if len(gyumolcsok[i])<5

rovid=[]
for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i])<5:
        print(gyumolcsok[i])

print(rovid)

rovid=[]
for e in gyumolcsok:
    if len(e)<5:
        rovid.append(e)
print(rovid)

rovid=[e for e in gyumolcsok if len(e)<5]
print(rovid)

rovid=[]
i=0
while i<len(gyumolcsok):
    if len(gyumolcsok[i])<5:
        rovid.append
    i+=1

print(rovid)

while True:
    if len(gyumolcsok[i-1])<5:
        rovid.appned(gyumolcsok[i])

    if len(gyumolcsok)==i:
        break

print(gyumolcsok[:2])

print(gyumolcsok[-2:])
print(gyumolcsok[len(gyumolcsok)-2:])

print(gyumolcsok[1:-1])

paratlan=gyumolcsok[1::2]
print(paratlan)

paros=gyumolcsok[::2]
print(paros)

masolat=gyumolcsok
print(masolat)
masolat.reverse()
print(" ".join(masolat))

print(",  ".join(masolat))


tabla=[]
for i in range(20):
      sor=[]
      for k in range(10):
          sor.append((i+1)*(k+1))
      tabla.append(sor)

#print(tabla)

oszlop=[]
for e in tabla:
   # print(e)
   oszlop.append(e[0])
print(oszlop)
print(oszlopVissza(5))
print(oszlopVissza(10))

oszlop=[e[:3]for e in tabla]
oszlop=[e[4:7] for e in tabla]
oszlop=[e[4:7] for e in tabla]
print(oszlop)

#függvény
#hánnyal osztható oszlopokat adjon
#bekérés, annyival osztható oszlopok kiírás
szam= int(input("adj meg egy  számot:"))

print(str(szam))

for i in range(1, 40):
    if i % szam == 0:
        print(i)













