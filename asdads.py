#file kezelés
f=open=("proba.txt," "w")
f.write("Hello")
f.write=("\n")
f.wite("vilag")

f.close()

f=open("proba.txt","r")

szoveg=f.read()

sorok=szoveg.split("\n")
print(sorok)

f.close()

f=open("poba.txt","r")
sorok=[]
for sor in f:
           sorok.append(sor.replace("\n"," ").replace("\r"," ")

print(sorok)
f.close()
