import math
X = int(input())
score = 100
count = 0
while score < X:
    count += 1
    score = math.floor(score*1.01)
print(count)
