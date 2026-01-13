S = input()
S = list(S)

# 貪欲法
# Wを左に詰めてく作業では？

ans = 0
W_cnt = 0

for i in range(len(S)):
    if S[i] == "W":
        ans += i - W_cnt
        W_cnt += 1

print(ans)