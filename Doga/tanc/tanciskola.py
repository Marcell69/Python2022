tancok=[]
f=open("tancrend.txt","r")
for e in f:
    e=e.replace("\n","")
    tancok.append(e)

f.close
print("2.feladat")
print("Az első: " , tancok[0] [0])
print("Az első: " , tancok[-1] [0])


print("3.feladat:")
#print(" {}.format(len(tancok)))

tancnevek=tancok[::3]
print(tancnevek)

#f=open("szereplok.txt","x")
#f.write
#lanyok=tancok[1::3]
#fiuk=tancok[2::3]

#f.close
