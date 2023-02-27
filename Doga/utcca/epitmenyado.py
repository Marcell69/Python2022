telkek=[]
f=open("utca.txt","r")
for e in f:
    e=e.replace("\n","")
    telkek.append(e)

f.close
telkek.pop(0)
print("2.feladat:")
print("A mintában {}telek szerepel.".format(len(telkek)))

print("3.feladat:")
adoszamBeker= input("Kérek egy adószámot: ")
szam=[]
for e in telkek:
   szam.append(e.split(" "))
for e in telkek:
    if e[0]==adoszamBeker:
        print(e[1],e[2])





