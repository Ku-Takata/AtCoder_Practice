N = int(input())
A = list(map(int,input().split()))

# 1から順番にソートした辞書に3つの要素窓を最大化する
cnt_num = {}

for a in A:
    if a not in cnt_num:
        cnt_num[a] = 1
    else:
        cnt_num[a] += 1

sort_num = sorted(cnt_num.items(), key=lambda item: item[0])
# print(sort_num)
ans = 0

if len(sort_num) >= 3:
    for i in range(1, len(sort_num)-1):
        cnt = sort_num[i][1]
        if sort_num[i][0] - sort_num[i-1][0] == 1:
            cnt += sort_num[i-1][1]
        if sort_num[i+1][0] - sort_num[i][0] == 1:
            cnt += sort_num[i+1][1]

        if cnt > ans:
            ans = cnt
elif len(sort_num) == 2:
    if sort_num[1][0] - sort_num[0][0] == 1:
        ans = sort_num[1][1] + sort_num[0][1]
    else:
        ans = max(sort_num[1][1], sort_num[0][1])
elif len(sort_num) == 1 or len(A) == 1:
    ans = sort_num[0][1]

print(ans)

# 41 デバッグ作業に時間がかかってしまった。もっとスマートに書けていればミスも少なかったかもしれない。
# 以下のように辞書の代わりにインデックスをaの値とし、初めに10^5+1分作れば簡単だった。
"""
l = [0] * 100005
ans = 0

for i in range(N):
    l[A[i]] += 1

for i in range(len(l) - 2):
    ans = max(ans, sum(l[i:i+3]))

print(ans)
"""