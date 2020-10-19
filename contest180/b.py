import math
N = int(input())
x = list(map(int, input().split()))
man = 0
yu = 0
che = []
for i in x:
    man += abs(i)
    yu += abs(i)**2
    che.append(abs(i))

print(man)
print(math.sqrt(yu))
print(max(che))