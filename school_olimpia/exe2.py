import math 

radius_1 = int(input())
radius_1 = radius_1
height_1 = int(input())
height_1 = height_1

V1 = (math.pi * radius_1 * radius_1 * height_1)/1000

radius_2 = int(input())
radius_2 = radius_2
height_2 = int(input())
height_2 = height_2

V2 = (math.pi * radius_2 * radius_2 * height_2)/1000

V1_round = round(V1,2)
V2_round = round(V2,2)


if V1_round > V2_round:
    print(V1_round)
elif V2_round > V1_round:
    print(V2_round)
else:
    print(V1_round)
