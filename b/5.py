N,L=map(int,input().split())
a=[]
for i in range(1,N):
    a.append(L+i-1)
print(a)
print(sum(a))