N = int(input())
A = list(map(int, input().split()))
ans = 0
count_max = 0
for i in range(2,1001):
    count = 0
    for j in range(N):
        if A[j]%i==0:
            count += 1
    if count > count_max:
        ans = i
        count_max = count
print(ans)
