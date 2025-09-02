from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x600')
        self.title('Tkinter using classes')

    def changestatus(self):
        if self.statusvar.get() == 'Ready':
            self.statusvar.set('Done')
        else:
            self.statusvar.set('Ready')

    def createButton(self, btnname):
        Button(text=btnname, command=self.changestatus, bg='black', fg='white').pack()

    def createStatusBar(self):
        self.statusvar = StringVar()
        self.statusvar.set('Ready')
        self.statusbar = Label(textvariable=self.statusvar, anchor=W, relief=SUNKEN, padx=5, pady=5, bg='black', fg='white')
        self.statusbar.pack(side=BOTTOM, fill=X)


if __name__ == '__main__':
    gui = GUI()
    gui.createButton('Change status')
    gui.createStatusBar()
    gui.mainloop()

    