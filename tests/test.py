    #Login
#user input
name = input("What's your name? ") # Bobby
age = input("How old are you? ") #20

if int(age) <= 17:
    print("You are too young for this site!")
else:
    print("You logged in successfully. ")

if name[0].capitalized() == "B":
    print("Your are welcome.")
else:
    print("You are not allowed")
    
