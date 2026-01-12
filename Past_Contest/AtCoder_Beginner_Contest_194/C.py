from collections import Counter

N = int(input())
A = list(map(int,input().split()))

cnt_A = Counter(A)

ans = 0
keys_A = list(cnt_A.keys())

for i in range(len(keys_A)):
    for j in range(i):
        a_i = keys_A[i]
        a_j = keys_A[j]

        ans += cnt_A[a_i] * cnt_A[a_j] * (a_i - a_j) ** 2

print(ans)