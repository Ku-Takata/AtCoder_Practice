N = int(input())
A = []

for i in range(N):
    A.append(int(input()))

# 2回押すことがあるということはループしているということ
# 2と書かれたボタンを押したら終了

# Counter = {2:1}になったら終了、Conter = {n:2} (n != 2)になったら-1で終了

cnt_manual = [(0,0)]*(N+1)
i = 0
cnt = 0

while cnt_manual[2][1] != 1:
    if cnt_manual[A[i]][0] == 0:
        cnt_manual[A[i]] = (A[i], 1)
        i = A[i]-1
        cnt += 1
    else:
        cnt = -1
        break

print(cnt)








"""
# 押す順番を格納
manual = []
i = 0

while A[i] not in manual:
    manual.append(A[i])
    i = A[i]-1
    if A[i] == 2:
        print(len(manual)+1)
        break

if A[i] != 2:
    print(-1)
"""