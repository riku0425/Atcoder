import math
N = int(input())
for i in range(1,1+int(math.sqrt(N))):
    if N%i==0:
        x = i
        y = N//i  

print(x-1+y-1)
