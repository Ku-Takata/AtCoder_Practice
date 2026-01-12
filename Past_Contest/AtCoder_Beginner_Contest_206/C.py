N = int(input())
A = list(map(int, input().split()))

# countによってO(N^2)になっている
"""
cnt = 0

for i in range(N-1):
    limit_A = A[i+1:]
    cnt += len(limit_A) - limit_A.count(A[i])

print(cnt)
"""

# ハッシュマップを使って、o(N)に留める
from collections import Counter

total_pairs = N * (N-1) // 2
cnt = Counter(A)
same_pairs = 0

for v in cnt.values():
    if v > 1:
        same_pairs += v * (v-1) // 2

ans = total_pairs - same_pairs

print(ans)