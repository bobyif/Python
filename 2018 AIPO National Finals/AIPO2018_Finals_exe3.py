alphabet = "abcdefghijklmnopqrstuvwxyz"
user_input = input("Enter the subsequence : ")
index = 0

for i in user_input:
    if i == alphabet[index]:
        index += 1
    else:
        None

print(index)