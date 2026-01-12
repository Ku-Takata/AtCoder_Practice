N = int(input())
A = list(map(int,input().split()))

right = [0] * (N+1)

for i in range(N-2,-1,-1):
    right[i] = right[i+1] + A[i+1]

ans = 0

for i in range(N):
    ans += A[i] * right[i]

ans %= (10**9 + 7)
print(ans)