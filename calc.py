import tkinter as tk

class Calc:
    key_positions = [
        (7,1,0), (8,1,1), (9,1,2), ('+',1,3),
        (4,2,0), (5,2,1), (6,2,2), ('-',2,3),
        (1,3,0), (2,3,1), (3,3,2), ('/',3,3),
        (0,4,0), ('.',4,1), ('=',4,2), ('*',4,3),
        ('C',5,0)
    ]


    def __init__(self, root):
        self.root = root
        self.root.geometry('380x555')
        self.root.resizable(False, False)
        self.root.title('Calculator - sandipv2')
        self.display_var = tk.StringVar()

    def calculate(self):
        tk.Entry(
            self.root, textvariable=self.display_var, font='lucida 24 bold', justify='right'
        ).grid(row=0, column=0, columnspan=4, ipadx=5, ipady=5, )

        for char, row, col in self.key_positions:
            self.make_keys(char, row, col)

    def key_click(self, event): 
        char = event.widget['text']

        if char == '=':
            try:
                result = eval(self.display_var.get())
                self.display_var.set(result)
            except Exception as e:
                self.display_var.set('Error')
        elif char == 'C':
            self.display_var.set('')
        else:
            self.display_var.set(self.display_var.get() + str(char))


    def make_keys(self, char, row, col):
        btn = tk.Button(self.root, text=char,width=6, height=3, font='lucida 15 bold')
        btn.bind('<Button-1>', self.key_click)
        btn.grid(row=row, column=col)

        if not str(char).isdigit():
            btn.config(bg='grey')

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calc(root)
    calc.calculate()
    root.mainloop()     