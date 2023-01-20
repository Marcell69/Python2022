def oszlopba(munkalista,db):
        for i in range(len(lista)):
            print(munkalista[i],end="  ")
        if  i%db==db-1:
                    print()
print()

lista=[]
for i in range (10):
        lista.append(int(input("Kérek egy számot:  ")))

lista=[123,24,45,26,26,75,23,57,87,12]

print(lista)

for i in range(len(lista)):
        print(lista[i],end="")
        if  i%3==2:
                    print()
print()

szamBe=int(input("Kérek egy számot:   "))
if szamBe in lista:
        print("van benne")
else:
        print("nincs benne")

oszlopba(lista,5)
