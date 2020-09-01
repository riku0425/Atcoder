N=int(input())
a=list(map(int,input().split()))

a=sorted(a,reverse=True)

alice=a[::2]
bob=a[1::2]


print(sum(alice)-sum(bob))