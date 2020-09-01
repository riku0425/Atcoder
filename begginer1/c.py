""" N=int(input())

a=list((int(x) for x in input().split()))
sum=0
for i in range(len(a)):
    if(a[i]%2==0):
        sum+=1
        for i in range(len(a)):
            if(a[i]%2==0):
                sum+=1
            else:
                break
    else:   
        break
print(sum) """

n=input()
a=list(map(int,input().split()))#リストで格納したい場合
cnt=0
while all(i%2==0 for i in a):　#内包表記
    a=[i/2 for i in a]
    cnt+=1
print(cnt)