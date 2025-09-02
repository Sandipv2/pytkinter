from tkinter import *
# import sys
# sys.exit()

def handleclick(e):
    print('Button clicked')
    print(e)

root = Tk()
root.title('Events')
root.geometry('400x400')

btn = Button(root, text='Click Me')
btn.pack()

# Single click
btn.bind('<Button>', handleclick) 

# Double click
btn.bind('<Double-1>', quit)

root.mainloop()