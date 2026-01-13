N,x = map(int,input().split())
A = list(map(int,input().split()))

sort_A = sorted(A)
cnt = 0

for i in range(N):
    if i != N-1:
        if x - sort_A[i] >= 0:
            cnt += 1
        elif x - sort_A[i] < 0:
            break
    else:
        if x - sort_A[i] == 0:
            cnt += 1

    x = x - sort_A[i]

print(cnt)

# 15