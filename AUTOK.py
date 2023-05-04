#készitsünk auto osztályt
#tul: szin,ajtokszáma,márka,tipus
#tudjon indulni indulaskor mondja WUTUTU
#duda mondja TÜTÜ
#irányjelző azt mondja KAT KAT
#leszármazott bmw
#bmw induljo ugy hogy WRUM
#iranyjelzo legyen nema
#másik class mercedes Duda: DUD
#audi check engine igaz vagy hamis ALAPBOL HAMIS

class auto:szin,ajtok,marka,tipus["",0,"",""]
    def __init__(self,szin,ajtok,marka,tipus):
         self.szin=szin
         self.ajtok=ajtok
         self.marka=marka
         self.tipus=tipus
    def indulas(self):
        print("Wututu")
    def szin(self):
        print("Az auto szine:{}".format(self.szin)
        
auto1=auto("Narancs",4,"Volkswagen","7R")
auto1.szin


