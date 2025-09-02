from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message boxes')
root.geometry('400x400')

def showinfo():
    messagebox.showinfo('Information', 'Mere bachche, always stay positive, far away from negativity, lust, jealousy, anger and greed. Always stay blissfull.')

def showwarn():
    messagebox.showwarning('Maine kaha tha na!', 'Ab pachtave kav hot, jab chidiya chug gai khet')

info = Button(root, text='Show info', command=showinfo)
info.pack()

warn = Button(root, text='Show warning', command=showwarn)
warn.pack()

# messagebox.askyesnocancel
# messagebox.askquestion
# messagebox.askokcancel

root.mainloop()