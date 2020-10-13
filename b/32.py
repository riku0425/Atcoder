N, K = map(int, input().split())
a=[]
def decode(N,K):
    if N>0:
        a.append(str(int(N%K)))
        return decode(int(N/K),K)
    else:
        # a.append(str(0))
        return "".join(a)
print(len(decode(N,K)))
