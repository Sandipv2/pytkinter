import tkinter as tk

root = tk.Tk()
root.title('Tkinter grid and vars')
root.geometry('400x400')

login_title = tk.Label(root, text='Log In', font='arial 20 italic')
login_title.grid(row=0, column=1)

name = tk.Label(root, text='Username: ')
name.grid(row=1, column=0)

password = tk.Label(root, text='Password: ')
password.grid(row=2, column=0)

user_var = tk.StringVar()
pass_var = tk.StringVar()

user_entry = tk.Entry(root, textvariable=user_var)
user_entry.grid(row=1, column=1)

pass_entry = tk.Entry(root, textvariable=pass_var)
pass_entry.grid(row=2, column=1)


def handle_submit():
    if not user_var.get() or not pass_var.get():
        return

    print(f'username: {user_var.get()}')
    print(f'password: {pass_var.get()}')
    user_var.set('')
    pass_var.set('')

submit_btn = tk.Button(root, text='Submit', command=handle_submit)
submit_btn.grid(columnspan=2)

root.mainloop()