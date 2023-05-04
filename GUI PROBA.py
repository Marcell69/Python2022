#Import the required libraries
import math
from tkinter import *


def eltol(pontok,x,y):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==0:
            vissza.append(pont+x)
        else:
            vissza.append(pont+y)
    return vissza

def nagyit(pontok,meret=1):
    vissza=[]
    for pont in pontok:
        vissza.append(pont*meret)
    return vissza

def forgat(pontok,szog):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i % 2==0:
            szogRadian=math.radians(szog)

            x= pontok[i]*math.cos(szogRadian) - pontok[i+1]*math.sin(szogRadian)

            y= pontok[i]*math.sin(szogRadian) + pontok[i+1]*math.cos(szogRadian)

            vissza.append(x)
            vissza.append(y)
    return vissza

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("600x700")

# Create a canvas widget
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
canvas.pack(fill = BOTH,expand = 1)

# Add a line in canvas widget

#pontok0 = [10,10,30,10,30,10,90,60,90,60,150,10,150,10,170,10,150,170,170,170,10,170,30,170,10,10,10,170,30,30,30,170,170,10,170,170,150,30,150,170,30,30,90,80,90,80,150,30]

M = [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10]
nev=[]
for i in range(5):
    nev.append(eltol(M,100*i,0))

for betu in nev:
    betu=nagyit(betu,0.5)
    betu=eltol(betu,50,700)
    nev[i]=betu
    #canvas.create_line(betu,fill="green",width=1)
    
    
canvas.create_line(M, fill="orange", width=5)


kozep=[0,0]
db=0
for betu in nev:
    xK=betu[::2]
    yK=betu[1::2]
    kozep[0]+=sum(xK)
    kozep[1]+=sum(yK)
    db+=len(xK)

kozep[0]/=db
kozep[1]/=db

szog=0
while True:
    canvas.delete("all")
    szog+=.5
    print(szog)
    for betu in nev:
        betu=eltol(betu,-kozep[0],-kozep[1])
        betu=forgat(betu,szog)
        betu=eltol(betu,kozep[0],kozep[1])

        canvas.create_line(betu, fill="red", width=3)

        win.update_idletasks()
        win.update()


    #win.mainloop()
