input = int(input("put integer : "))


dictionary = {}
def funt(input):
    i = 1
    while i <= input:
        dictionary[i] = i*i
        i = i + 1  
    return dictionary

print(funt(input))