N = int(input())
b=0
for i in range(1,29):
    for j in range(1,41):
        if 3**j + 5**i == N:
            print(j,i)
            exit()
print(-1)