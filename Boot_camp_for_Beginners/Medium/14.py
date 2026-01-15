H,W = map(int,input().split())
painting = []

for i in range(H):
    painting.append(list(input()))

# 上下左右全部.で囲まれていたらできない、そうでないならできる
if H >= 2 and W >= 2:
    for i in range(H):
        for j in range(W):
            if painting[i][j] == "#":
                if i == 0:
                    if j == 0:
                        if painting[i+1][j] == "." and painting[i][j+1] == ".":
                            print("No")
                            exit()
                    elif j == W-1:
                        if painting[i+1][j] == "." and painting[i][j-1] == ".":
                            print("No")
                            exit()
                    else:
                        if painting[i+1][j] == "." and painting[i][j+1] == "." and painting[i][j-1] == ".":
                            print("No")
                            exit()
                elif i == H-1:
                    if j == 0:
                        if painting[i-1][j] == "." and painting[i][j+1] == ".":
                            print("No")
                            exit()
                    elif j == W-1:
                        if painting[i-1][j] == "." and painting[i][j-1] == ".":
                            print("No")
                            exit()
                    else:
                        if painting[i-1][j] == "." and painting[i][j+1] == "." and painting[i][j-1] == ".":
                            print("No")
                            exit()
                else:
                    if j == 0:
                        if painting[i+1][j] == "." and painting[i][j+1] == "." and painting[i-1][j] == ".":
                            print("No")
                            exit()
                    elif j == W-1:
                        if painting[i+1][j] == "." and painting[i][j-1] == "." and painting[i-1][j] == ".":
                            print("No")
                            exit()
                    else:
                        if painting[i+1][j] == "." and painting[i-1][j] == "." and painting[i][j+1] == "." and painting[i][j-1] == ".":
                            print("No")
                            exit()
elif H == 1 and W >= 3:
    for i in range(H):
        for j in range(1,W-1):
            if painting[i][j] == "#":
                if painting[i][j-1] == "." and painting[i][j+1] == ".":
                    print("No")
                    exit()
elif H >= 3 and W == 1:
    for i in range(1,H-1):
        for j in range(W):
            if painting[i][j] == "#":
                if painting[i-1][j] == "." and painting[i+1][j] == ".":
                    print("No")
                    exit()
elif H == 2 and W == 1:
    if painting[0][0] != painting[1][0]:
        print("No")
        exit()
elif H == 1 and W == 2:
    if painting[0][0] != painting[0][1]:
        print("No")
        exit()
else:
    if painting[0] == "#":
        print("No")
        exit()

print("Yes")

# 30 鬼の条件分岐コードになってしまった。2次元空間系はこうなってしまう傾向がある。練習の必要あり。
# 他の人のコードを参考に、短いコードを書いてみた

H, W = map(int,input().split())
painting = [input() for i in range(H)]

dirs = [
    (-1,0), (0,1),
    (1,0), (0,-1)
]

for i in range(H):
    for j in range(W):
        if painting[i][j] == "#":
            for dy,dx in dirs:
                # 行列の周り4辺を除いて上下左右に#が存在したときはOK
                if (0 <= i+dy < H) and (0 <= j+dx < W):
                    if painting[i+dy][j+dx] == "#":
                        break
            else:
                print("No")
                exit()

print("Yes")