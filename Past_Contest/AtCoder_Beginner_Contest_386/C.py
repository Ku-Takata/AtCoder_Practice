K = int(input())
S = input()
T = input()

if abs(len(S) - len(T)) > 1:
    print("No")
    exit()

i = 0
min_len = min(len(S), len(T))

# 初めて違う文字列が現れたインデックスを調べる
while i < min_len and S[i] == T[i]:
    i += 1

# 1つだけ変更
if len(S) == len(T):
    if S[i+1:] == T[i+1:]:
        print("Yes")
    else:
        print("No")

# 1つ挿入
elif len(T) - len(S) == 1:
    if S[i:] == T[i+1:]:
        print("Yes")
    else:
        print("No")

# 1つだけ削除
elif len(S) - len(T) == 1:
    if S[i+1:] == T[i:]:
        print("Yes")
    else:
        print("No")

# 60 問題自体は簡単だが、それを実装するのが大変だった。