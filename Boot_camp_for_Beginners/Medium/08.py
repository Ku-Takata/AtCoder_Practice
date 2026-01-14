N = int(input())
A = list(map(int,input().split()))

color = [0]*9

for a in A:
    if a < 3200:
        color[a // 400] = 1
    else:
        color[-1] += 1

if sum(color[:8]) == 0 and color[8] >= 2:
    print(1, sum(color))
else:
    print(sum(color[:8]), sum(color))

# 11 条件分岐パレードにならずに解けた