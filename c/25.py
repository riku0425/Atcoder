import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
num_list = list(itertools.permutations(range(1,n+1)))
print(abs(num_list.index(p)-num_list.index(q)))
