from tkinter import *

root = Tk()
root.title('Icons and more')
root.geometry('500x500')

# .ico files only on windows
# On Linux, Tkinter only supports .xbm (X11 bitmap) for iconbitmap.
# Note the "@" before the filename — Tkinter needs it for .xbm.)
# root.wm_iconbitmap('@python.xbm')

icon = PhotoImage(file='mern.png')
root.iconphoto(False, icon)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f'{width}x{height}')

root.mainloop()