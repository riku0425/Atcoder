import math
N,D = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
ans=0
print(X)
for i in range(N):
    for j in range(i+1,N):
        dist=0
        for p in range(D):
            print(dist)
            dist+=(X[i][p]-X[j][p])**2
        if dist==int(dist):
            ans+=1