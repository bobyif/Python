input = input("put someting : ")

class InputOutString(object):
    def __init__(self):
        self.input = input

    def printString(self):
        print (self.input.upper())

strObj = InputOutString()
strObj.printString()