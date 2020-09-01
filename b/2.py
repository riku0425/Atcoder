n = int(input())
sp = []
for i in range(n):
    s,p = map(str, input().split())
    sp.append((s,int(p),i+1))


sp=sorted(sp,key=lambda x: (x[0],-x[1]))

for i in range(n):
    print(sp[i][2])