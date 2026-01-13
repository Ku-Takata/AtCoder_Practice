X = int(input())
i = 3

# 偶数はスキップしたら早そう
while i < X:
    if X % 2 == 0:
        X += 1
        i = 3
    else:
        if X % i == 0:
            X += 1
            i = 3
        else:
            i += 1

    # print(X, i)

print(X)