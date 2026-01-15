H,W = map(int,input().split())
A = [[0] * W for _ in range(H)]

for i in range(H):
    temp = input()
    for j in range(W):
        A[i][j] = temp[j]

A_0 = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] == ".":
            if "#" not in A[i]:
                continue
            elif not any(A[k][j] == '#' for k in range(H)):
                continue
        A_0[i][j] = (A[i][j])

# print(A_0)

A_rev = []

for i in range(H):
    output = ""
    for j in range(W):
        if A_0[i][j] != 0:
            output += A_0[i][j]

    if output != "":
        print(output)

# 60 実装に時間がかかりすぎた。初めて使った表現もあり、大変だった。
# 初めて使ったのはanyと出力を溜めておくoutputの部分。また、行列の初期化が慣れていなかった。
# zip（転置）を使うと簡単そうなのでもう一度解いてみた。
H,W = map(int,input().split())
A = []

for i in range(H):
    a = input()
    if "#" in a:
        A.append(a)

A = list(zip(*A))
A_rev = []

for a in A:
    if "#" in a:
        A_rev.append(a)

A_rev = zip(*A_rev)

for a in A_rev:
    print(*a, sep="")