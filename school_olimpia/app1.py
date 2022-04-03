user_input= input("Enter the String : ")


def only_upper(x):
    upper_chars = 0
    for char in x:
        if char.isupper():
            upper_chars += 1
    return upper_chars

def only_lower(y):
    lower_chars = 0
    for char in y:
        if char.islower():
            lower_chars += 1
    return lower_chars



numbers = sum(c.isdigit() for c in user_input)
others  = len(user_input) - numbers - only_upper(user_input) - only_lower(user_input)
print(f"Digits count : {numbers}")
print(f"Lowercase letters count: {only_lower(user_input)}")
print(f"Uppercase letters count: {only_upper(user_input)}")
print(f"Other symbols count: {others}")
