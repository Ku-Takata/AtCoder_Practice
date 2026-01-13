s = int(input())
a = []
i = 0

while len(a) == len(set(a)):
    if i == 0:
        pass
    elif s % 2 == 0:
        s = s // 2
    else:
        s = 3*s + 1

    a.append(s)
    i += 1

# 初めに被る値のインデックス+1 = リストの長さ
print(len(a))