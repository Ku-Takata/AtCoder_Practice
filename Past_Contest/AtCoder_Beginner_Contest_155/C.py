from collections import Counter

N = int(input())
S = ["".join(input()) for i in range(N)]

cnt = Counter(S)
max_value = max(cnt.values())

max_keys = [k for k,v in cnt.items() if v == max_value]

sort_max_keys = sorted(max_keys)

print("\n".join(sort_max_keys))