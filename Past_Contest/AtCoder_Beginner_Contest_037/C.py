N,K = map(int, input().split())
A = list(map(int, input().split()))

"""
ruisekiwa = 0

for i in range(N-K+1):
    ruisekiwa += sum(A[i:i+K])

print(ruisekiwa)
"""

# 全体*(N-K+1) - 余剰分でやってみる
ans = sum(A) * (N-K+1)

for i in range(N-K+1):
    zyouyo = A[i] * (N-K-i) + A[-(i+1)] * (N-K-i)
    ans -= zyouyo

print(ans)