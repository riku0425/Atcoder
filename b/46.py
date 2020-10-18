X, Y = map(int,input().split())
a = False
for turtule in range(X+1):
    turu = X - turtule
    num = turtule*4 + turu*2
    if num == Y:
        print("Yes")
        exit()
print("No")