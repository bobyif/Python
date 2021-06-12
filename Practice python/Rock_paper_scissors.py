user1 = input("what are you going to put? ")
user2 = input("What are you going to put? ")

if user1.lower() == "rock" and user2.lower() == "scissors":
        print("user1 won")
elif user1.lower() == "scissors" and user2.lower() == "paper":
    print("user1 won")
elif user1.lower() == "paper" and user2.lower() == "rock":
    print("user1 won")
elif user1 == user2:
    print("Tie")
else:
    print("user2 won")