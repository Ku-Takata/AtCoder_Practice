N = int(input())
RC = []

for i in range(N):
    RC.append(list(map(int,input().split())))

# x,yそれぞれ独立で最大最小の値を調べて、それぞれの真ん中の場所を調べる
max_x = 0
max_y = 0
min_x = float("inf")
min_y = float("inf")

for i in range(N):
    if RC[i][0] > max_x:
        max_x = RC[i][0]
    if RC[i][1] > max_y:
        max_y = RC[i][1]
    if RC[i][0] < min_x:
        min_x = RC[i][0]
    if RC[i][1] < min_y:
        min_y = RC[i][1]

import math

middle_x = math.ceil((max_x - min_x) / 2)
middle_y = math.ceil((max_y - min_y) / 2)

print(max(middle_x, middle_y))

# 25 解法が分からず調べたが、実装は自分で上手くできたと思う。
# ceilよりも+1して//2した方が良かったのと、if文をRとC別々で格納していれば、if文なしで記述できそう。