from tkinter import *

def kg_g_p_ou():
    grams = float(e1_var.get()) * 1000
    t1.insert(END,grams)
    pounds = float(e1_var.get()) * 2.20961
    t2.insert(END,pounds)
    ounces = float(e1_var.get()) * 35.264
    t3.insert(END,ounces)

window = Tk()

window.title("Multi-widget_GUI")

l1= Label(window, height=3, width=10, text="current value : ")
l1.grid(row = 1, column = 1)

e1_var = StringVar()
e1 = Entry(window, textvariable = e1_var)
e1.grid(row = 1, column = 2)

b1 = Button(window, height=1, width=10, text="Convert", command=kg_g_p_ou)
b1.grid(row = 1, column = 3)

t1 = Entry(window)
t1.grid(row = 2, column = 1)

t2 = Entry(window)
t2.grid(row = 2, column = 2)

t3 = Entry(window)
t3.grid(row = 2, column = 3)

t4 = Entry(window)
t4.grid(row = 3, column = 2

window.mainloop()
