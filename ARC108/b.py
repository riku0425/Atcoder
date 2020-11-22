import re,collections,time
start = time.time()
N = int(input())
s = input()
l = []
# for _ in range(100):
#     s = (s.replace("fox",""))
# print(len(s))
# print(time.time()-start)


for i in range(N):
    l.append(s[i])
    if len(l)>=3:
        if l[-1]=="x" and l[-2]=="o" and l[-3]=="f":
            l.pop()
            l.pop()
            l.pop()
print(len(l))
print(time.time()-start)
        