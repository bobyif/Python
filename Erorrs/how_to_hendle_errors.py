def devide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Sorry you can't divide by 0"

print(devide(1,0))