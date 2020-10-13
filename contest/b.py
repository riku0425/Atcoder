H, W = map(int, input().split())
l=[]
count=0
for _ in range(H):
    s = input()
    l.append(s)

for i in range(H):
    for j in range(W-1):
        if l[i][j] =="." and l[i][j+1] == ".":
            count+=1

for j in range(W):
    for i in range(H-1):
        if l[i][j]=="." and l[i+1][j]==".":
            count+=1
print(type(l[0]))
print(type(l[0][1]))
print(count)