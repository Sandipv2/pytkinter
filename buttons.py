import tkinter as tk

root = tk.Tk()

root.geometry('400x400')
root.title("Tkinter Buttons")

################ Defs ###################
def name():
    print("Name is sandip")

def age():
    print("age is 19")

btn_frame = tk.Frame()
btn_frame.pack(side='left', anchor='nw')

name_btn = tk.Button(btn_frame, text='Name', command=name)
name_btn.pack(side='left')

age_btn = tk.Button(btn_frame, text='Age', command=age)
age_btn.pack()

label = tk.Label(text='Response here.')
label.pack()



root.mainloop()