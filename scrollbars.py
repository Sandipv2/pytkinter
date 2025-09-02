from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('Scrollbar')

text = Text(root, font='arial 20 bold')
text.pack(side=LEFT, fill=BOTH, expand=True)
text.focus_set()

scrollbar = Scrollbar(root, command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)

text.config(yscrollcommand=scrollbar.set)

root.mainloop()