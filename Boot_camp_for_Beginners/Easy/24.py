A, B, M = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
ticket = []

for i in range(M):
    ticket.append(list(map(int,input().split())))

# まずはチケットを使ったときの値段を調べる
ans_ticket = float("inf")

for i in range(M):
    total = A_list[ticket[i][0]-1] + B_list[ticket[i][1]-1] - ticket[i][2]
    if total < ans_ticket:
        ans_ticket = total

# チケットが使えない組み合わせを調べる
ans_no_ticket = min(A_list) + min(B_list)

if ans_no_ticket < ans_ticket:
    print(ans_no_ticket)
else:
    print(ans_ticket)

# 25