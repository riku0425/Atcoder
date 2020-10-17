import sys
N = int(input())
A = list(map(int, input().split()))
score = 10**18
total = 1
if 0 in A:
    print(0)
else:
    for i in range(len(A)):
        total *= A[i]
        if total>score:
            print(-1)
            sys.exit()
    print(total)