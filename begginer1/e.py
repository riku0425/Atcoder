""" N,a,b=map(int,input().split())
sum=0
for i in range(1,N+1):
    j=i
    if(i<10):
        if(i>=a and i<=b):
            sum+=i
    else:
        lst=[]
        while j>0:
            lst.append(j%10)
            j//=10
        lst.reverse()
        c=lst[0]+lst[1]
        if(c>=a and c<=b):
            sum+=i
            

print(sum) 
一部正解したが完答にはならなかった
"""
# 入力
N,A,B=map(int,input().split())

c=0
for x in range(1,N+1):
    y=list(str(x))
    # 各桁の和を求める
    z=sum([int(a) for a in y])
    # 各桁の和がA以上B以下なら加算
    if A<=z and z<=B:
        c+=x

# 出力
print(c)
