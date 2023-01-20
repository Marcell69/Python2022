#1
szamok=[]
for i in range(8):
        szamok.append (int(input("kérek egy számot: ")))
#2
print(szamok)
#3
for i in range(8):
        print(szamok[i],end=" ")
        if  i%4==3:
                print()
#4            
osszeg=sum(szamok)
print("A számok összege:",osszeg)

#5

szoveg="Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."
print(szoveg)

#6
#7

betu=" "
while betu!="end":
            betu=input("Kérek egy betűt:   ")
            szoveg1=szoveg.count(betu)
            print(szoveg1)

#8
print(szoveg[::-1])

#9
print("Szöveg mérete:  ",len(szoveg))
szoveg=szoveg.replace("orna"," ")
print(szoveg)

print("Szöveg új mérete:  ",len(szoveg))


