import random
#100000 középsikolás szül.dátum
f=open("datum.txt","w")
i=0
while i!=100000:
    i+=1
    ev = random.randint(2003,2008)
    hon = random.randint(1,12)
    if hon == 1 or hon == 3 or hon == 5 or hon == 7 or hon == 8 or hon == 10 or hon == 12:
        nap = random.randint(1,31)
    elif hon == 4 or hon == 6 or hon == 9 or hon == 11:
        nap = random.randint(1,30)
    if ev % 4 == 0:
        nap = random.randint(1,29)
    else:
        nap = random.randint(1,28)
    ev = str(ev)
    hon = str(hon)
    nap = str(nap)
    f.write(ev + "." + hon + "." + nap  + "\n")
    
f.close()
