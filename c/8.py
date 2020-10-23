# L, R = map(int, input().split())
# mod = 2019
# i = L % mod
# j = R % mod
# for k in range(i,j+1):
#     for l in range()
# print(i*(1+i) % mod)

l,r = map(int,input().split())
if (r-l)>=2019: #2019の倍数があるので
  print(0)
else:
  mini = 2018
  for i in range(l,r+1):#全探索
    for j in range(i+1,r+1):
      ans = ( i*j )% 2019
      mini = min(ans,mini)
  print(mini)