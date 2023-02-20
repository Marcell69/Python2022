f=open("valaszok.txt")

adatok=f.read().split("\n")

adatok.remove("")

f.close()


helyes=adatok[0]
adatok.remove(helyes)

valaszok=[]
for e in adatok:
    valaszok.append(e.split(" "))

print("2.feladat:A vetélkedőn" +str(len(valaszok))+"versenyző indult. ")

versenyzo=input("3.feladat: A versenyző azonosítója - ")

for e in valaszok:
        if e[0]==versenyzo:
            print(e[1]+"\t (a versenyző válasza)")
            print(e[1]+"\t  (a veresenyző válassza)")
print("()\t (a versenyző válassza)".format([e[1] for e in valaszok if e[0]==versenyzo][0]))

print("4feladat:  ")
print(helyes+"\t(a helyes megoldás")
print(valaszok[1])

for sorszam.betu in enumerate(versenyzoValasza):
    if betu==helyes(sorszam):
            print("+",end="")
    else:
        print("  ",end=" ")

print("\t (a versenyző helyes válaszai)")

feladat = input("5.feladat: A feladat sorszáma = ")

db=0
for e in VersenyzoValasza:
    if e[1] (feladat) ==helyes(feladat):
        db+=1

print("A feladatra [0] fő, a versenyzők [1]-a adott helyes választ.".format(db,db/len(valaszok)))

