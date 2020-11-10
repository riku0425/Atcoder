import sys
N = input()
k = len(N)

ans = 10**9
update = False
for i in range(2**k):
    res = []
    for j in range(k):
        #print(j>>k)
        if (i>>j) &1:
            res.append(N[j])
    #print(res)
    l = len(res)
    if l==0:
        if int(N)%3 == 0:
            print(0)
            sys.exit()
        else:
            continue  
    res = "".join(res)
    #print(res)
    res = int(res)
    if res %3==0:
        ans = min(ans,k-l)
        update = True
if update: print(ans) 
else:print(-1)