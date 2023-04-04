adatok= []
f=open("snooker.txt")
for e in f:
        e=e.replace("\n","").split(";")
        adatok.append(e)
f.close
mezonevek=adatok.pop(0)
#print(mezonevek)
print("3. feladat: A világranglistán {} veresenyző szerepel.".format(len(adatok)))

fizetes= []
for x in adatok:
    fizetes.append(int(x[3]))
összeg= sum(fizetes)
atlag= összeg/len(fizetes)
#print("atlag:",atlag)

print("4.feladat a versenyzök átlagosa {:.2f} fontot keresetek".format(atlag))

kpenz=[]
for k in adatok:
    if k[2]=="Kína":
        kpenz.append(int(k[3]))
legjobb=(max(kpenz))

for e in adatok:
    if e[3]==str(legjobb):
        print("5.feladat: A legjobban kereső kínai versenyző: \n Helyezés: {} Név: {} \n Ország: {} \n Nyeremény összege: {}Ft".format(e[0],e[1],e[2],e[3]))

for e in adatok:
    if  e[2] =="Norvégia":
        print ("6.feladat: A versenyzők kozott van norvég versenyző")

Kína=0
Anglia=0
Wales=0
Skócia=0
for fo in adatok:
    if fo[2]=="Skócia":
        Skócia+=1
    if fo[2]=="Anglia":
        Anglia+=1
    if fo[2]=="Wales":
        Wales+=1
    if fo[2]=="Kína":
        Kína+=1

#print(Kína)
#print(Anglia)
#print(Wales)
#print(Skócia)

print("7.feladat: Statisztika \n \t Kína - {} fő \n \t Anglia - {} fő \n \t Wales - {} fő \n \t Skócia - {} fő".format(Kína,Anglia,Wales,Skócia))
