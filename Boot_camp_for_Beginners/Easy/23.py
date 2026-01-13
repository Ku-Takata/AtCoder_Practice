N = int(input())
D, X = map(int,input().split())
A = []

for i in range(N):
    A.append(int(input()))

choco_list = [0] * N

for i in range(N):
    day = 1
    while day + A[i] <= D:
        choco_list[i] += 1
        day = day + A[i]


ans = N + X + sum(choco_list)
print(ans)

# 10