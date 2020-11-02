A, B, C = map(int, input().split())
MOD = 998244353

score = A*(A+1)*B*(B+1)*C*(C+1)/8 %MOD
print(score)
ans = 0
for a in range(1,A+1):
    for b in range(1,B+1):
        ans += a*b
print(ans*C*(C+1)/2%MOD)