from collections import Counter

N = int(input())
A = list(map(int, input().split()))

mod_A = []
ans = 0

for i in range(N):
    mod_A.append(A[i] % 200)

cnt = Counter(mod_A)

for v in cnt.values():
    ans += v * (v-1) // 2

print(ans)