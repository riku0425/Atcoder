N=int(input())
sum=0
name=[]
for _ in range(N):
    a,b=map(int,input().split())
    if(a==b):
        sum+=1
        if(sum==3):
            name.append("Yes")
    else:
        sum=0
    
if len(name)==0:
    print("No")
else:
    print("Yes")