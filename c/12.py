# import collections
# N = int(input())
# char = list(input() for _ in range(N))
# count = 0
# for i in range(N):
#     for j in range(i+1,N):
#         if collections.Counter(char[i]) == collections.Counter(char[j]):
#             count += 1
# print(count)
        
import collections

N = int(input())
s = ["".join(sorted(input())) for _ in range(N)]
c = collections.Counter(s)
# print(s)
# print(c)
count = 0
for si in set(c):
    n = c[si]
    count += n*(n-1)/2
print(int(count))