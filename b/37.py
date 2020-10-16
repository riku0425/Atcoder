N, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
judge = total/(4*M)
score = 0
for i in range(len(A)):
    if A[i] >= judge:
        score +=  1
if score >= M:
    print("Yes")
else:
    print("No")