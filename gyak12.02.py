lista=["2022.12.0100:58:45Karcsi",
            "2022.12.0101:05:06Karcsi",
            "2022.12.0101:17:37Béla",
            "2022.12.0107:06:20Juci",
            "2022.12.0110:33:05Karcsi",
            "2022.12.0114:24:23Karcsi",
            "2022.12.0114:41:11Juci",
            "2022.12.0115:54:45Béla",
            "2022.12.0118:49:11Juci",
            "2022.12.0122:01:42Béla",
            "2022.12.0122:19:31Béla",
            "2022.12.0123:43:24Béla"]
print(lista)
ora=input("Kérek egy órát:    ")

for e in lista:
        if e[10:12]   == ora:
            print(e[18: ])

nev=input("Adj meg egy nevet:  ")
for e in lista:
        if e [18: ] == nev:
            print(e[10:18])
            
