x = int(input())
y = int(input())

def f(x, y):
    if x <= y:
        print((x - 1,y - 2) + (x-2,y-1) + 2)
    else:
        print(x-2,y-2 + 1)
f(x,y)