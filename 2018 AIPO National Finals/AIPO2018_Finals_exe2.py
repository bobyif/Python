n = int(input("How many card do you have : "))

numbers = []

def all_numbers(numbers):
    for i in range(0,100):
        numbers.append(i)

def sorting(numbers):
    user_number = input("Enter your cards :")
    for num in user_number.split(" "):
        num = int(num)
        if num in numbers:
            numbers.remove(num)
        else:
            print("ops")
    print(numbers)

all_numbers(numbers)
sorting(numbers)
