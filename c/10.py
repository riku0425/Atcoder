N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
for i in range(N):
    if b[i] <= a[i]:
        count += b[i]
    elif a[i] < b[i] and b[i] <= a[i] + a[i+1]:
        count += b[i]
        a[i+1] = a[i+1] + a[i] - b[i]
    else:
        count += a[i] + a[i+1]
        a[i+1] = 0
print(count)