A, B, X = map(int, input().split())
# x_keta = len(str(X))-2
# print(x_keta)
# max_score = 0
# for i in range(10**(x_keta-1),10**x_keta):
#     if A*i+B*(x_keta) <= X:
#         max_score = max(max_score, i)
    
# print(max_score)

def ok(N):
    return A * N + B * len(str(N)) <= X
left = 0
right = 10**9+1
while right - left > 1:
    middle = (right + left)//2
    if ok(middle):
        left = middle
    else:
        right = middle
print(left)