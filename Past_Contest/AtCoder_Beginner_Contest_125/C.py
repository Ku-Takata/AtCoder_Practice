from math import gcd

N = int(input())
A = list(map(int, input().split()))

"""
Combinatation = N*(N-1)//2
gcd_list = []

for i in range(N-1):
    for j in range(i+1, N):
        gcd_list.append(gcd(A[i], A[j]))

ans = max(gcd_list)

print(ans)
"""

left = [0] * (N+1)
right = [0] * (N+1)

for i in range(N):
    left[i+1] = gcd(left[i], A[i])

for i in range(N-1, -1, -1):
    right[i] = gcd(right[i+1], A[i])

ans = 0

for i in range(N):
    current_gcd = gcd(left[i], right[i+1])
    ans = max(ans, current_gcd)

print(ans)