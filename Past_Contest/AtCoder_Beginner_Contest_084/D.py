import math

Q = int(input())
Q_list = []

for i in range(Q):
    l, r = map(int, input().split())
    Q_list.append([l,r])

# 素数判定(N)
def is_prime(n):
    if n < 2:
        return 0

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0

    return 1

# 素数判定(N + 1 / 2)
def is_2017like(n):
    n = (n + 1) / 2
    if n < 2:
        return 0

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0

    return 1

# 累積素数カウント
cs = [0] * (10**5 + 2)

for i in range(2, 10**5+1):
    if is_prime(i) == 1 and is_2017like(i) == 1:
        cs[i+1] = cs[i] + 1
    else:
        cs[i+1] = cs[i]

for l,r in Q_list:
    ans = cs[r+1] - cs[l]
    print(ans)