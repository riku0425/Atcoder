N = int(input())
a = list(int(input()) for _ in range(N))
a_max = max(a)
a_sort = sorted(a)
number = a.index(a_max)
for i in range(N):
    if i == number:
        print(a_sort[len(a)-2])
    else:
        print(a_max)