user_input = int(input("Enter a number :"))

d = dict()

for i in range(1, user_input + 1):
    d[i] = i*i

print(d)