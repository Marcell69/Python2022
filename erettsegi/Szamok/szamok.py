import random
f=open("felszam.txt","r")

kerdesek=[]
for sor in f:
        josor=sor.replace("\n"," ")
        josor2=f.readline ().replace("\n"," ")
        temp=josor2.split("  ")

        kerdesek.append([josor, int(temp[0]), int(temp[1]), temp[2]])

        
f.close()

print("2. feladat")
print("az adatfile-ban"  + str(len(kerdesek))+ "kérdés van.")

matek=[]
for e in kerdesek:
         if e[3]=="matematika":
                 matek.append(e[2])

print("Az adatfajban  " + str(len(matek)) +
                "matematika feladat van,  1 pont er " + str(matek.count(1)) +
                "feladat, 2pontot er " +str(matek.count(2)) +
                "feladat, 1pontot er " +str(matek.count(3)) + "feladat.")

valaszok=[]
for e in kerdesek:
        valaszok.append(e[1])

valaszok=(e[1] for e in kerdesek)
print("A válaszok számértéke ()-től ()-ig tart. ".format(min(valaszok),max(valaszok)))

temakork=[]
for e in kerdesek:
        if e[3] not in temakorok:
                temakork.append(e[3])
                
print("5. feladat")
print("A témakörök:  "+".2.  ".join(temakorok))

print("6.feladat")

beker=input("Milyen témaköröből szeretne kérdést kapni? ")
ujLista=[e for e in kerdesek if e[3]==beker]

sorsolt=random.choice(ujLista)

valasz=input (sorsolt[0])
if int(valasz)==sorsolt[1]:
        print(str(sorsolt[2])+"  pont")
else:
        print("0pont")
        print("A helyes válasz.  "+ sorsolt[1])

print("7. feladat")

lista10=[]
for i in range(10):
        r=radnom.choice(kerdesek)
        while r in lista10:
                r=random.choice(kerdesek)

        lista10.append(r)

print(lista10)

random.shuffle(kerdesek)
lista10=kerdesek[0:10]

print(len(lista10))

f=open("tesztfel.txt","w")
for e in lista10:
        f.write(str(e[2]) + " "+str(e[1])+" "+str(e[0])+"\n")
                

f.write("A feladatsorra összesen [0]pont adható".format(ossz))
f.close()





















        
