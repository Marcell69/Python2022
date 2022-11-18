
lista=["bence" , "lászló" , "ferenc"]
lista.append ("Martin")

try:
                print(lista[3])
except:
                print("Valami nem jó!")
else:
                print("Sikeres lefutás.")
finally:
                print("ez a vége")

szam=""
while szam=="":

                try:
                                szam=int(input("Kérek egy számot:   "))
                except ValueError as e:
                                print(e)
                                print("Ez nem szám")
                except:
                                print("Ismeretlen hiba")


print=(szam)


