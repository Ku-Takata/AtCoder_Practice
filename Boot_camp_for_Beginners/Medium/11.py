N,M = map(int,input().split())
ab = []
cd = []

for i in range(N):
    ab.append(list(map(int,input().split())))

for i in range(M):
    cd.append(list(map(int,input().split())))

# マンハッタン距離が近く、番号が小さい座標を求める

for a,b in ab:
    distance = float("inf")
    for i in range(len(cd)):
        if abs(a-cd[i][0]) + abs(b-cd[i][1]) < distance:
            distance = abs(a-cd[i][0]) + abs(b-cd[i][1])
            ans = i+1

    print(ans)

# 16 問題内容も実装も難しくなかった。