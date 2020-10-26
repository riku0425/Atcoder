n = int(input())
p = list(map(int, input().split()))

num = p[0]
ans = 1

for i in range(1, n):
    if num >= p[i]:
        ans += 1
        num = p[i]

print(ans)