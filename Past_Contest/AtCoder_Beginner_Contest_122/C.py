N,Q = map(int,input().split())
S = input()

# TLE, 累積和を使おう
"""
Q_list = []
cnt_list = []

for i in range(Q):
    Q_element = list(map(int, input().split()))
    Q_list.append(Q_element)

for l,r in Q_list:
    AC_cnt = S[l-1:r].count("AC")
    cnt_list.append(AC_cnt)

for i in range(len(cnt_list)):
    print(cnt_list[i])
"""

# 部分文字列でACを列挙して辞書に格納, 激遅
"""
Q_list = []
sub_dict = {}
AC_cnt_list = []

for i in range(Q):
    Q_element = list(map(int, input().split()))
    Q_list.append(Q_element)

for i in range(N-1):
    for j in range(1,N+1):
        if i < j:
            sub_dict[i,j] = S[i:j+1].count("AC")

for l,r in Q_list:
    AC_cnt_list.append(sub_dict[l-1,r-1])

for i in range(Q):
    print(AC_cnt_list[i])
"""

# 累積和
ruisekiwa = [0] * (N-1)

for i in range(N-1):
    if S[i:i+2] == "AC":
        ruisekiwa[i] = ruisekiwa[i-1] + 1
    else:
        ruisekiwa[i] = ruisekiwa[i-1]

for i in range(Q):
    l,r = map(int, input().split())
    if l == 1:
        AC_cnt = ruisekiwa[r-2]
    else:
        AC_cnt = ruisekiwa[r-2] - ruisekiwa[l-2]
    print(AC_cnt)