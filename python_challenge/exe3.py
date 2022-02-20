import re


user_input = int(input("Write a fact : "))

value = 1
def fact(user_input,value):
    while user_input != 0:
        value = value * user_input
        user_input -= 1
    return value

print(fact(user_input,value))