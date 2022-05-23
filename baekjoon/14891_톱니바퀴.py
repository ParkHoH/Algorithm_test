board = [[]]
for _ in range(4):
    board.append(input())

for _ in range(int(input())):
    n, direction = map(int, input().split())
    checked = [False] * 5
    checked[n] = True
    stack = [[n, direction]]
    rotate = [[n, direction]]

    while stack:
        num, direct = stack.pop()
        if num in range(1, 5):
            if num-1 in range(1, 5) and not checked[num-1] and board[num][-2] != board[num-1][2]:
                checked[num-1] = True
                stack.append([num-1, -direct])
                rotate.append([num-1, -direct])
            if num+1 in range(1, 5) and not checked[num+1] and board[num][2] != board[num+1][-2]:
                checked[num+1] = True
                stack.append([num+1, -direct])
                rotate.append([num+1, -direct])

    while rotate:
        num, direct = rotate.pop()
        if direct == 1:
            board[num] = board[num][-1] + board[num][:-1]
        else:
            board[num] = board[num][1:] + board[num][0]

score = 0
for i in range(1, 5):
    if i == 1 and board[i][0] == "1":
        score += 1
    elif i == 2 and board[i][0] == "1":
        score += 2
    elif i == 3 and board[i][0] == "1":
        score += 4
    elif i == 4 and board[i][0] == "1":
        score += 8

print(score)