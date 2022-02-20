#ex3

user_input = int(input("1 :"))

i = 0
def func(x, i):
    while i <= user_input:
        i = i + 1
    
    return x * func(x - 1)

x = user_input
print(func(x, i))