import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
board.append([0] * (N+1))
for _ in range(N):
    board.append([0] + list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(2, N+1):
        board[i][j] += board[i][j-1]

for i in range(1, N+1):
    for j in range(2, N+1):
        board[j][i] += board[j-1][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    num = board[x2][y2] - board[x2][y1-1] - board[x1-1][y2] + board[x1-1][y1-1]
    print(num)