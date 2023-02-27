
def ido2mp():
    pass

eredmenyek=[]

f=open("triatlon.txt")
for egySor in f:
    temp=egySor.replace("\n"," ").split(";")
    eredmenyek.append(temp)

f.close()

eredmenyek.pop(0)

print("2.feladat")
print("A versenyen [] versenyző indult.".format(len(eredmenyek)))

print("3.feladat")

