N = int(input())
a = []
xy = []
for i in range(N):
    a.append(int(input()))
    for _ in range(a[i]):
        xy.append(list(map(int, input().split())))
