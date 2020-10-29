# import math
A, B = map(int, input().split())
# print(int(A * B / math.gcd(A, B)))

def gcd(a, b):
    while max(a, b) % min(a, b) != 0:
        a, b = b, a%b
    return b
def lcm(a, b):
    return int(a * b / gcd(a,b))
print(lcm(A, B))