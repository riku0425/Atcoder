import math
A, B = map(str, input().split())
p=int(A)
q=int(B[0]+B[2]+B[3])
print(p*q//100)
# print(math.floor(A*B))
# print('{:.20f}'.format(A*B))