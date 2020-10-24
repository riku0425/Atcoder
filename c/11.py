N = int(input())
h = list(map(int, input().split()))
num_min = 10**20
for i in range(N-1):
    if h[i] == h[i+1]:
        continue
    elif h[i] + 1 <= h[i+1] :
        h[i+1] -= 1
    else:
        print("No")
        exit() 
print("Yes")