N = int(input())
v = sorted(list(map(int, input().split())))
count = 0
ave = []
ave.append((v[0]+v[1])/2)
for i in range(N-2):
    ave.append((ave[i]+v[i+2])/2)
print(ave[-1])
