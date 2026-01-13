S = input()

# 左から見たときと右から見たときで考える
left = [0]*(len(S)+1)
right = [0]*(len(S)+1)

for i in range(len(S)):
    if S[i] == "<":
        left[i+1] = left[i] + 1

for i in range(len(S)):
    if S[-i-1] == ">":
        right[-i-2] = right[-i-1] + 1

numbers = [0]*(len(S)+1)

# maxの方を取る
for i in range(len(left)):
    numbers[i] = max(left[i], right[i])

ans = sum(numbers)
"""
print(left)
print(right)
print(numbers)
"""
print(ans)