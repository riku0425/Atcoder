N = int(input())
# def getDivisors(n: int):
#     # validation check
#     if not isinstance(n, int):
#         raise("[ERROR] parameter must be integer")
#     if n < 0:
#         raise("[ERROR] parameter must be not less than 0 (n >= 0)")

#     lowerDivisors, upperDivisors = [], []
#     i = 1
#     while i * i <= n:
#         if n % i == 0:
#             lowerDivisors.append(i)
#             if i != n // i:
#                 upperDivisors.append(n//i)
#         i += 1
#     return lowerDivisors + upperDivisors[::-1]

# # 約数列挙
# a = getDivisors(N)
# for i in a:
#     print(i)
i=1
div = []
while i*i <=N:
    if N%i==0:
        div.append(i)
        if i!=N//i:
            div.append(N//i)
    i += 1
div.sort()
for i in div:
    print(i)
        