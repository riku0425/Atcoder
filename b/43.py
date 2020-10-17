A, B, C, K = map(int, input().split())
count = 0

if (A>=K):
    count = K
else:
    count = A -(K-A-B)
print(count)