N, K = map(int,input().split())
S = [int(input()) for i in range(N)]

"""
ans = 0

if 0 in S:
        ans = N
else:
    for i in range(N):
        cnt = 0
        total = S[i]
        for j in range(i+1, N):
            if total <= K:
                total *= S[j]
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0

print(ans)
"""

total = 1
right = 0
left = 0
ans = 0

if 0 in S:
    ans = N
    print(ans)
    exit()

for right in range(N):
    total *= S[right]

    while total > K and left <= right:
        total //= S[left]
        left += 1

    ans = max(ans, right - left + 1)

print(ans)