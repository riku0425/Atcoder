N = list(input())
num = 0
for i in N:
    num += int(i)
if num % 9 == 0:
    print("Yes")
else:
    print("No")