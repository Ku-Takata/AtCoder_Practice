N,K = map(int, input().split())
P = list(map(int, input().split()))
kitaichi = [(x+1) / 2 for x in P]
sums = [0.0] * (N+1)

# 期待値の合計を前から順番に足し合わせ、リストsumsに値を格納
for i in range(N):
    sums[i+1] = sums[i] + kitaichi[i]

ans = 0

# 今までの最大期待値と次の期待値のどちらが大きいか判定
for i in range(N-K+1):
    ans = max(ans, sums[i+K] - sums[i])

print(ans)