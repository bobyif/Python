user_input= input("Enter the String : ")
  

all_freq = {}
  
for i in user_input:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  

answer = 0
for i in all_freq.values():
    if i >= 3:
        answer += 1
    else:
        answer += 0

if answer == 1:
    print("NO")
else:
    print("YES")