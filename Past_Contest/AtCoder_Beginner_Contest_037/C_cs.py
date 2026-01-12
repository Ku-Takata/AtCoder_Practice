N, K = map(int, input().split())
A = list(map(int, input().split()))

ruisekiwa = [0] * (N+1)

for i in range(N):
    ruisekiwa[i+1] += ruisekiwa[i] + A[i]

# print(ruisekiwa)

ans = 0

for i in range(N-K+1):
    # 区間和 = 1番目から区間終わりの和 - 1番目から区間始まりの和
    kukan_sum = ruisekiwa[i+K] - ruisekiwa[i]
    ans += kukan_sum

print(ans)