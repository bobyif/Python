import random
i = 0

while True:
    i+=1
    number_guess = random.choice(range(1,9))
    user1 = input("Guess the number or type 'exit' to leave.")
    if user1 == "exit":
        break
    if user1 == "":
        continue
    if int(user1) < number_guess:
        print("too low")
    elif int(user1) > number_guess:
        print("too hight")
    else:
        print("You got it right!")
print(i)