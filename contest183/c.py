from itertools import permutations
def main():
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        T.append(list(map(int,input().split())))

    ans = 0
    for per in permutations(range(1,N)):
        score = 0
        prev = 0
        for i in range(N-1):
            cur = per[i]
            score += T[prev][cur]
            # print(prev,per)
            prev = cur
            # print(cur)
        score += T[prev][0]

        if score == K:
            ans += 1
    print(ans)
main()
# if __name__ =="__main__":
#     main()