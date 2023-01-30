
f=open("felszam.txt","r")

for sor in f:
        josor=sor.replace("\n","")
        josor2=f.readline().replace("\n"," ")
        temp=josor2.split("  ")

        kerdesek.append([josor, int(temp[0]), int(temp[1]), temp[2]])

        
        print(temp)

f.close()
print(kerdesek)
print("az adatfile-ban"  + len(kerdesek)+ "kérdés van.")
