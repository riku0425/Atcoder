N, A, B = map(int, input().split())
blue = "b"
red = "r"
c = []
while N>len(c):
    for _ in range(A):
        c.append(blue)
        if N<=len(c):
            break
    for _ in range(B):
        c.append(red)
        if N<=len(c):
            break
print(c)
print(c.count("b"))