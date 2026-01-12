N = int(input())
S = input()

west_cs = [0] * (N+1)
east_cs = [0] * (N+1)
ans = float('inf')

for i in range(N):
    if S[i] == "W":
        west_cs[i+1] = west_cs[i] + 1
        east_cs[i+1] = east_cs[i]
    else:
        west_cs[i+1] = west_cs[i]
        east_cs[i+1] = east_cs[i] + 1

# リーダーの左で西に向いている人の数＋右で東に向いている数
for i in range(N):
    ans = min(ans, west_cs[i] + (east_cs[N] - east_cs[i+1]))

print(ans)