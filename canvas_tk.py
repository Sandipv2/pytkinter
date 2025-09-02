from tkinter import *

root = Tk()

root.title('Canvas in TK')
root.geometry('500x500')

# Disable resize
root.resizable(False, False)

canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Lines
canvas.create_line(0,0,500,500, fill='red')
canvas.create_line(0,500, 500, 0, fill='blue')

# Rectangles
canvas.create_rectangle(250, 250, 375, 375, fill='yellow')
canvas.create_rectangle(125, 125, 250, 250, fill='green')
canvas.create_rectangle(125, 250, 250, 375, fill='red')
canvas.create_rectangle(250, 125, 375, 250, fill='blue')

# Ovals
canvas.create_oval(50, 50, 150, 100, fill='white')
canvas.create_oval(200, 20, 300, 120, fill='red')

# Text
canvas.create_text(250, 250, text='Canvas!!', font='arial 25 bold',)

root.mainloop()