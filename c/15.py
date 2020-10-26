N = int(input())
b = list(map(int, input().split()))
dic = []
dic.append(b[0])
dic.append(b[-1])
for i in range(1,len(b)):
    dic.append(min(b[i-1],b[i]))
print(sum(dic))