import math
S, P = map(int, input().split()) 
judge = math.sqrt(S**2-4*P)
# if str(judge
# print(judge)
a = (S+judge)/2
b = (S-judge)/2
if a<=0 or b<=0:
    print("No")
    exit()
if (S+judge)%2!=0 or (S-judge)%2!=0:
    print("No")
    exit()
print("Yes")