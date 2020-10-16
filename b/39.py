N, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
if N>=total:
    print(N-total)
else:
    print("-1")