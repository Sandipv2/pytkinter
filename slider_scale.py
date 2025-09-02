from tkinter import *

root = Tk()
root.title('Scale / Slider')
root.geometry('500x500')

def handlewidth(e):
    root.geometry(f'{slider2.get()}x{slider1.get()}')

def handleheight(e):
    root.geometry(f'{slider1.get()}x{slider1.get()}')

# vertical slider
slider1 = Scale(root, from_=0, to=500, length=300)
slider1.set(500)
slider1.pack()

# horizontal slider
slider2 = Scale(root, from_=0, to=500,orient=HORIZONTAL, tickinterval=150, length=300)
slider2.set(200)
slider2.pack()

slider2.bind("<ButtonRelease-1>", handlewidth)
slider1.bind("<ButtonRelease-1>", handleheight)

root.mainloop()