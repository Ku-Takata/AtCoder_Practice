N = int(input())
travel = [[0,0,0]]

for i in range(N):
    travel.append(list(map(int,input().split())))

# print(travel)

for i in range(N):
    step = travel[i+1][0] - travel[i][0]
    if abs(travel[i+1][1] - travel[i][1]) + abs(travel[i+1][2] - travel[i][2]) <= step:
        if (abs(travel[i+1][1] - travel[i][1]) + abs(travel[i+1][2] - travel[i][2])) % 2 == 0 and step % 2 == 0:
            ans = "Yes"
        elif (abs(travel[i+1][1] - travel[i][1]) + abs(travel[i+1][2] - travel[i][2])) % 2 == 1 and step % 2 == 1:
            ans = "Yes"
        else:
            ans = "No"
            break
    else:
        ans = "No"
        break

print(ans)

# 23 出力が全て大文字にしてしまって、それに気づくのに時間がかかった。
# 他は特に問題なくできた。マンハッタン距離の問題は得意かもしれない。ただもっと短くコードは書けると思う。