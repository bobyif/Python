user_input = int(input("1 :"))

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = user_input
print(fact(x))