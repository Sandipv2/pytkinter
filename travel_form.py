from tkinter import *
from tkinter import messagebox
import json
import os

root = Tk()

root.title('Varma Travels')
root.geometry('600x400')

Label(root, text='Varma Travels', font='comicsans 18 bold').grid(row=0, column=3, columnspan=3, pady=15)

def handlesubmit():
    record = {
        "name": namevar.get(),
        "age": agevar.get(),
        "phone": phonevar.get(),
        "email": emailvar.get(),
        "from": fromvar.get(),
        "to": tovar.get(),
        "want_food_and_beverages": wantfoodvar.get()
    }

    if os.path.exists('records.json'):
        with open('records.json', 'r') as f:
            try:
                data = json.load(f)
            except Exception:
                data = []
    else:
        data = []

    data.append(record)

    with open('records.json', 'w') as f:
        json.dump(data, f, indent=4)

    messagebox.showinfo("Success", "Form submitted successfully!")

    namevar.set('')
    agevar.set(0)
    phonevar.set('')
    emailvar.set('')
    fromvar.set('')
    tovar.set('')

####### Labels #######
namelabel = Label(root, text="Name")
agelabel = Label(root, text="Age")
phonelabel = Label(root, text="Phone")
emaillabel = Label(root, text="Email")
fromlabel = Label(root, text="From")
tolabel = Label(root, text="To")

namelabel.grid(row=1, column=0)
agelabel.grid(row=2, column=0)
phonelabel.grid(row=3, column=0)
emaillabel.grid(row=4, column=0)
fromlabel.grid(row=5, column=0)
tolabel.grid(row=6, column=0)


####### Vars #######
namevar = StringVar()
agevar = IntVar()
phonevar = StringVar()
emailvar = StringVar()
fromvar = StringVar()
tovar = StringVar()
wantfoodvar = IntVar(value=0)


####### Entries #######
nameentry = Entry(root, textvariable=namevar)
ageentry = Entry(root, textvariable=agevar)
phoneentry = Entry(root, textvariable=phonevar)
emailentry = Entry(root, textvariable=emailvar)
fromentry = Entry(root, textvariable=fromvar)
toentry = Entry(root, textvariable=tovar)

nameentry.grid(row=1, column=1)
ageentry.grid(row=2, column=1)
phoneentry.grid(row=3, column=1)
emailentry.grid(row=4, column=1)
fromentry.grid(row=5, column=1)
toentry.grid(row=6, column=1)


####### Checkbuttons #######
foodcheckbtn = Checkbutton(root, text='Want food and beverages?', variable=wantfoodvar,)
foodcheckbtn.grid(row=7, column=1)


####### Buttons ########
submitbutton = Button(root, text='Sumit Details', command=handlesubmit)
submitbutton.grid(row=8,column=1)

root.mainloop()