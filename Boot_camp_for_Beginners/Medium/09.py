A,B,C = map(int,input().split())

# Aの数ずつ足して割ったあまりを格納してループしていることが分かったらNO
mod_list = {}
A_ini = A
ans = "NO"

while 2 not in mod_list.values():
    if A % B == C:
        ans = "YES"
        break
    else:
        mod = divmod(A,B)[1]
        if mod in mod_list:
            mod_list[mod] += 1
        else:
            mod_list[mod] = 1

        A += A_ini

if ans == "YES":
    print(ans)
else:
    print("NO")

# 30 辞書型のデバッグ作業に時間がかかった。辞書型の勉強の必要あり。