import math
A, B, C, D = map(int, input().split(' '))
CD_least_common = C * D // math.gcd(C, D)
except_cnt = B // C - (A - 1) // C + B // D - (A - 1)// D - (B // CD_least_common - (A - 1) // CD_least_common)
print(B - (A - 1) - except_cnt)