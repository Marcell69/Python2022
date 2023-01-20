import random

def szoBeker():
    szo=input("Kérek egy szót:  ")
    if szo=="":
        jelentes=""
    else:
        jelentes=input(szo+ "  jelentes:   ")
    return (szo,jelentes)

print(szoBeker())


szavak=[]
def sokBeker():
    szo=szoBeker()
    while szo[0]!="":
        szvak.append(szo)
        szo=szoBeker()

    return szavak
        
def filebaIr(lista):
    f=open("szotar.txt","a")

    for e in lista:
            f.write("  ".join(e))
            f.write("\n")
    f.close()

kerdesek=[]
def beolvas():
        f=open("szotar.txt","r")
        for sor in f:
            kerdesek.append(sor.replace("\n"," ").split("  "))

        f.close()
        
def kerdez():
    print(kerdesek)

beolvas()
kerdez()
    
        

    # szavak=szoBeker()
    # filebaIr(szavak)
