import math
N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]
total = 0
for i in range(N-1):
    for j in range(i+1,N):
        total += math.sqrt((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)*2*math.factorial(N-1)
print(total/math.factorial(N))