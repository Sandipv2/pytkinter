from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Radiobutotns')
root.geometry('500x400')

def orderfood():
    if not food.get():
        messagebox.showerror('Food not selected!', 'Food select to karo!')
        return
    
    messagebox.showinfo('Order', f'Your order "{food.get()}" has been booked!! Thank You!')
    food.set('')

Label(root, text='What would you love to eat?', font='lucida 20 bold').pack()

food = StringVar()
food.set('')

Radiobutton(root, text='Veg Biryani', value='Biryani', variable=food).pack(anchor=W)
Radiobutton(root, text='Pohe', value='Pohe', variable=food).pack(anchor=W)
Radiobutton(root, text='Paneer Roti', value='Paneer Roti', variable=food).pack(anchor=W)
Radiobutton(root, text='Dosa', value='Dosa', variable=food).pack(anchor=W)

Button(root, text='Order food', command=orderfood).pack(anchor=W, padx=5, pady=5)

root.mainloop()