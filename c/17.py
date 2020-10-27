N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.append([A[i],i+1])
ans.sort()
score = []
for j in ans:
    score.append(j[1])
print(*score)