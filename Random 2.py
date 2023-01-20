# 3jegyű szám bekérés
szam="12"
while len(szam) !=3:
        szam=input("Kérek egy 3 jegyű számot:  ")

szam=int(szam)

if szam%12==0:
        print("osztoo")

print(szam)

szoveg="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(szoveg.split("  ")))
szoveg2=szoveg.replace("i","I")
print(szoveg2)
