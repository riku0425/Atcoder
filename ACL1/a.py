import numpy as np
N=int(input())
data_list = [ list(map(int,input().split())) for i in range(N)]
lx=np.sort(data_list,axis=0)#xについて
ly=np.sort(data_list,axis=1)
for i in range(N):
    x=data_list[i][0]