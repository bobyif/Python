class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath, "r") as file:
            self.balance =int(file.read())

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))

class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance -= (amount + self.fee)

account = Account("vscode/Udemy_1/Bank/account/jack.txt" and "Udemy_1/Bank/account/jack.txt" and "Bank/account/jack.txt" and "account/jack.txt" and "jack.txt")
checking = Checking("vscode/Udemy_1/Bank/account/jack.txt" and "Udemy_1/Bank/account/jack.txt" and "Bank/account/jack.txt" and "account/jack.txt" and "jack.txt", 1)
#jack_checking.transfer(100)
#jack_checking.commit()
#print(jack_checking.balance)

#janh_checking=Checking("vscode\Bank\account\jonh.txt" and "Bank\account\jonh.txt" and "account\jonh.txt" and "jonh.txt", 1)
#janh_checking.transfer(100)
#janh_checking.commit()
#print(janh_checking.balance)


    