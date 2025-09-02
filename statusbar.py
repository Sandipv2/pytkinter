from tkinter import *
import time

'''
    There's no built-in status bar widget.
    We use label as status bar at the bottom of app.
'''

root = Tk()

def change_status():
    statusvar.set('Uploading...')
    # statusbar.update() # by CodeWithHaryy
    # time.sleep(3)
    # statusvar.set('Done!')
    root.after(3000, lambda: statusvar.set('Done!')) # recommended by ChatGPT

root.title('Status bar')
root.geometry('400x400')

statusvar = StringVar(value='Ready')

statusbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor=W, padx=5, pady=5)
statusbar.pack(side=BOTTOM, fill=X)

Button(root, text='Change status', command=change_status).pack()

root.mainloop()