from tkinter import *

root = Tk()
root.title('Menus and Sub-menus')
root.geometry('600x500')

########## File Edit About ##########
# mainmenu = Menu(root)
# mainmenu.add_command(label='File')
# mainmenu.add_command(label='Edit')
# mainmenu.add_command(label='About')

def save():
    print('file saved')

mainmenu = Menu(root)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Open', command=save)
filemenu.add_command(label='Open folder', command=save)
filemenu.add_separator()
filemenu.add_command(label='Save', command=save)
filemenu.add_command(label='Save as', command=save)

editmenu = Menu(mainmenu, tearoff=0)
editmenu.add_command(label='Copy', command=save)
editmenu.add_command(label='Paste', command=save)
editmenu.add_command(label='Cut', command=save)
editmenu.add_command(label='Replace in file', command=save)

mainmenu.add_cascade(label='File', menu=filemenu)
mainmenu.add_cascade(label='Edit', menu=editmenu)
mainmenu.add_command(label='Exit', command=quit)

root.config(menu=mainmenu)

root.mainloop()