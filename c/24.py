import math
N = int(input())
for i in range(N, 10**5+4):
    flag = True
    for j in range(2,int(math.sqrt(N))+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)
        exit(0)
