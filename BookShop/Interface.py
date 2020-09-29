from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), Aulthor_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(), Aulthor_text.get(), year_text.get(), ISBN_text.get())
    list1.delete(0,END)
    search_command()

def updates_command():
     

window = Tk()

# Text 
l1_left = Label(window, text=("Title"))
l1_left.grid(row=0,column=0)

l2_left = Label(window, text = ("Year"))
l2_left.grid(row=2, column=0)

l1_right = Label(window, text=("Author"))
l1_right.grid(row=0, column=2)

l2_right = Label(window, text=("ISBN"))
l2_right.grid(row=2, column=2)

#Text entry

title_text=StringVar()
e1_left = Entry(window, textvariable=title_text)
e1_left.grid(row=0, column=1)

Aulthor_text=StringVar()
e1_right = Entry(window, textvariable=Aulthor_text)
e1_right.grid(row=0, column=3)

year_text=StringVar()
e2_left = Entry(window, textvariable=year_text)
e2_left.grid(row=2, column=1)

ISBN_text=StringVar()
e2_left = Entry(window, textvariable=ISBN_text)
e2_left.grid(row=2, column=3)

# Configuring LISTBOX and SCROLLBAR

list1 = Listbox(window, height=9, width=45)
list1.grid(row=3, column=0, rowspan= 6, columnspan= 2)

sb1 = Scrollbar(window)
sb1.grid(row=3, column=2, rowspan= 8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Configuring Buttons for the program

b1 = Button(window, text= "View all", width= 15, command=view_command)
b1.grid(row=3, column= 3) 

b1 = Button(window, text= "Search entry", width= 15, command=search_command)
b1.grid(row=4, column= 3)

b1 = Button(window, text= "Add entry", width= 15, command=add_command)
b1.grid(row=5, column= 3)

b1 = Button(window, text= "Update selected", width= 15, command=updates_command)
b1.grid(row=6, column= 3)

b1 = Button(window, text= "Delete selected", width= 15)
b1.grid(row=7, column= 3)

b1 = Button(window, text= "Close", width= 15)
b1.grid(row=8, column= 3)

mainloop()