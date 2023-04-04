import copy

class Myclass:
    x=5
    def megnovel(self,mennyivel=1):
        self.x+=mennyivel

class kutya:
    nev,fajta,agresszivitas,kor,szin=["","",0,0,""]
    def _init_ (self,nev,fajta,agresszivitas,kor,szin):
        self.nev=nev
        self.fajta=fajta
        self.agresszivitas=agresszivitas
        self.kor=kor
        self.szin=szin
        
    def ugat(self):
        print("vau-vau")

    def koszon(self):
        print("vau-vau, {} vagyok").format(self.nev)

    def talalkozas(self,masik):
        if self.agresszivitas>5 or masik.agresszivitas>5:
            if self.agresszivitas>=masik.agresszivitas:
                print("Meg halsz!")
            else:
                print(" NE bants báttyám!")
        else:
            if self.agresszivitas>=masik.agresszivitas:
                print("Sevasz kutya gyerek!")
            else:
                print("Szeva báttya!")

k1=kutya("Bodri","puli",3,9,"fekete")
k2=kutya("Morzsi","golden retriver",1,3,"világos barna")

k1.ugat()
k1.koszon()
k2.koszon()

k2.talalkozas(k1)
k1.talalkozas(k2)


"""
print(Myclass.x)

pl=Myclass()
print(pl.x)
p2=Myclass()
p2.x=1
print(p2.x)

pl.megnovel()
pl.megnovel(10)
print(pl.x)
"""
