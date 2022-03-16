p = 3.14159265359

userinput = input("Enter stats : ")

r1,h1,r2,h2 = userinput.split(",")


r1 = int(r1) / 10
r2 = int(r2) / 10
h1 = int(h1) / 10
h2 = int(h2) / 10

v1 = p * r1 * r1 * h1
v2 = p * r2 * r2 * h2

if v1 > v2:
    print(round(v1,2))

else:
    print(round(v2,2))


