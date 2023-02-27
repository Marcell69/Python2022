def darabol(sor):
        lista = sor.split("*")
        temp=lista[-1].split(" ")
        lista.pop(-1)

        lista+=temp
    
        return lista
#print(darabol("rn3.swc.com*20/Jul/1995:00:02:14*GET /history/apollo/apollo-13/apollo-13-patch.jpg*200 90112"))


naplo=[]
f =open("NASAlog.txt")
for e in f:
    naplo.append(darabol(e.strip()))
    
f.close()
#print(naplo[:10])
print("5.feladat: kérések száma: {}".format(len(naplo)))
