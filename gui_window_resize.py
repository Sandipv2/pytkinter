from tkinter import *

root = Tk()

def handleResize():
    root.geometry(f'{widthvar.get()}x{heightvar.get()}')

root.title('Window resizer')
root.geometry('500x400')
root.resizable(False, False)

Label(root, text='Window Resizer', font='comicsans 20 bold').grid(row=0, column=2)


##### Label #####

width_label = Label(root, text='Width: ')
width_label.grid(row=2, column=0)

height_label = Label(root, text='Height: ')
height_label.grid(row=3, column=0)

####### Entries ########

widthvar = IntVar(value=500)
heightvar = IntVar(value=400)

widthentry = Entry(root, textvariable=widthvar).grid(row=2, column=2)
heightentry = Entry(root, textvariable=heightvar).grid(row=3, column=2)

###### Button #####

Button(root, text='Resize', command=handleResize).grid(row=4, column=2)

root.mainloop()