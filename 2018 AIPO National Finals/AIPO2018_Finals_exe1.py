s = input("Firts word : ")
t = input("Second word : ")

def reversed(s):
    reversedString = ""
    index = len(s)
    while index > 0:
        reversedString += s[index - 1]
        index = index - 1
    return(reversedString)



if reversed(s) == t:
        print("Yes")
else:
        print("No")