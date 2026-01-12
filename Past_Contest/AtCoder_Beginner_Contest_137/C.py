from collections import Counter

N = int(input())
S = ["".join(sorted(input())) for i in range(N)] # 順番に入力をsortしてリストに格納

cnt = Counter(S)
total = 0

# 組み合わせをvalueごとに計算
for v in cnt.values():
    total += v*(v-1) // 2

print(total)