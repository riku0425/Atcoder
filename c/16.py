N, K, Q = map(int, input().split())
a = list(int(input()) for _ in range(Q))
b = [K-Q] * N
for i in a:
    b[i-1] += 1
for j in b:
    if j <=0:
        print("No")
    else:
        print("Yes")