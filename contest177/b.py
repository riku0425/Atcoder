import re
S=input()
T=input()
ans=10**1000

for i in range(len(S)-len(T)+1):
    score=0
    u=S[i:i+len(T)]
    for j in range(len(T)):
        if u[j]!=T[j]:
            score+=1
    ans=min(ans,score)
print(ans)