# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x500+1200+00")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, bg='pink')
canvas.pack(fill = BOTH, expand = 1)

#canvas2=Canvas(win, width=500, height=300, bg='pink')
#canvas2.pack(fill = BOTH, expand = 1)


# Add a line in canvas widget
#canvas.create_line(100,200,200,35, fill="green", width=5)
#canvas.create_line(0,0,200,35,20,300, fill="orange", width=10)
#win.mainloop()
canvas.create_line(200,200,200,35, fill="skyblue", width=10)
canvas.create_line(400,200,400,35, fill="skyblue", width=10)
canvas.create_line(400,40,200,40, fill="skyblue", width=10)
canvas.create_line(200,190,400,190, fill="black", width=10)


