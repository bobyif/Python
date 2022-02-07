a1 = input("width 1 :")
b1 = input("height  1 :")
a2 = input("width 2 :")
b2 = input("height  2 :")
s1 = int(a1)* int(b1)
s2 = int(a2)* int(b2)
if s1 < s2:
    print(s2)
elif s1 > s2:
    print(s1)
else:
    print("they are the same")
