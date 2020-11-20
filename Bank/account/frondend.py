#frontend.py
from tkinter import *
from acc import *
     
class Window(object):
     
    def __init__(self,window):
     
        self.window = window
        
        self.path = "vscode\bank\account\jack.txt" and "bank\account\jack.txt" and "account\jack.txt" and "jack.txt"

        window.geometry('1080x750')    

        self.window.wm_title("Bank")
     
        l1=Label(window,text="Deposit", pady = 50, font=("Helvetica", 30), bg="lightgrey")
        l1.grid(row=2,column=4)
     
        self.depost_text=StringVar()
        self.e1=Entry(window,textvariable=self.depost_text ,bd = 7, width = 25)
        self.e1.grid(row=4,column=3)

        b1=Button(window,text="deposit", width=12,command=self.deposit, bd = 6)
        b1.grid(row=4,column=5)

        self.list1=Listbox(window, height=6,width=35)
        self.list1.grid(row=4,column=4, padx = 20)
     

        l2=Label(window,text="Withdraw", pady = 50, font=("Helvetica", 30), bg="lightgrey")
        l2.grid(row=5,column=4)
     
        self.withdraw_text=StringVar()
        self.e2=Entry(window,textvariable=self.withdraw_text,bd = 7, width = 25)
        self.e2.grid(row=7,column=3)

        b2=Button(window,text="withdraw", width=12,command=self.withdraw, bd = 6)
        b2.grid(row=7,column=5)

        self.list2=Listbox(window, height=6,width=35)
        self.list2.grid(row=7,column=4, padx = 20)

        l3=Label(window,text="Transfer", pady = 50, font=("Helvetica", 30), bg="lightgrey")
        l3.grid(row=8,column=4)
     
        self.transfer=StringVar()
        self.e3=Entry(window,textvariable=self.transfer,bd = 7, width = 25)
        self.e3.grid(row=9,column=3)

        b3=Button(window,text="View all", width=12,command=self.transfer1, bd = 6)
        b3.grid(row=9,column=5)

        self.list3=Listbox(window, height=6,width=35)
        self.list3.grid(row=9,column=4, padx = 20)

     
    def deposit(self):
        a = self.e1.get()
        account.deposit(int(a))
        account.commit()
        with open(self.path, "r") as file:
            self.balance =int(file.read())
            self.full_balance = ("Your current balnce is :",self.balance,"lv")
            self.list1.insert(END,self.full_balance)

    def withdraw(self):
        b = self.e2.get()
        account.withdraw(int(b))
        account.commit()
        with open(self.path, "r") as file:
            self.balance =int(file.read())
            self.full_balance = ("Your current balnce is :",self.balance,"lv")
            self.list2.insert(END,self.full_balance)

    def transfer1(self):
        c = self.e3.get()
        checking.transfer(int(c))
        checking.commit()
        with open(self.path, "r") as file:
            self.balance =int(file.read())
            self.full_balance = ("Your current balnce is :",self.balance,"lv")
            self.list3.insert(END,self.full_balance)

window=Tk()
window.configure(bg="lightgrey") 
Window(window)
window.mainloop()

