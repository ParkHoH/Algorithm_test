n,m = 0,0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0]*5 for _ in range(5)]
def OOB(x,y):
    return x < 0 or x >= n or y < 0 or y >= m

def play(board,curx,cury,opx,opy):
    global visit
    if visit[curx][cury]: return 0
    canWin = 0
    for i in range(4):
        nx, ny = curx + dx[i], cury + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        if visit[nx][ny] or board[nx][ny] == 0:
            continue

        visit[curx][cury] = True
        opResult = play(board,opx,opy,nx,ny)+1
        visit[curx][cury] = False

        # 현재 저장된 값 패배인데 상대가 졌다고 하면 이기는 경우로 저장
        if canWin % 2 == 0 and opResult % 2 == 1 : canWin = opResult
        # 현재 저장된 값 패배인데 상대가 이겼다고 하면 최대한 늦게 지는 횟수 선택
        elif canWin % 2 == 0 and opResult % 2 == 0 : canWin = max(canWin,opResult)
        # 현재 저장된 값 승리인데 상대가 졌다고 하면 최대한 빨리 이기는 횟수 선택
        elif canWin % 2 == 1 and opResult % 2 == 1 : canWin = min(canWin,opResult)
    return canWin

def solution(board, aloc, bloc):
    global n,m
    n, m = len(board), len(board[0])
    return play(board,aloc[0],aloc[1],bloc[0],bloc[1])


# dir = ((-1,0),(0,1),(1,0),(0,-1))

# def A_turn(ar,ac,br,bc,cnt,board):
#     if board[ar][ac] == 0:
#         return (1,cnt)
#     winner = []
#     loser = []
#     flag = False
#     for dr,dc in dir:
#         nr,nc = ar+dr,ac+dc
#         if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:
#             flag = True
#             temp = [row[:] for row in board]
#             temp[ar][ac] = 0
#             iswin,turn = B_turn(br,bc,nr,nc,cnt+1,temp)
#             if iswin:
#                 winner.append(turn)
#             else:
#                 loser.append(turn)
#     if flag:
#         if winner:
#             return (0,min(winner))
#         else:
#             return (1,max(loser))
#     else:
#         return (1,cnt)


# def B_turn(br,bc,ar,ac,cnt,board):
#     if board[br][bc] == 0:
#         return (1,cnt)
#     winner = []
#     loser = []
#     flag = False
#     for dr,dc in dir:
#         nr,nc = br+dr,bc+dc
#         if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:
#             flag = True
#             temp = [row[:] for row in board]
#             temp[br][bc] = 0
#             iswin,turn = A_turn(ar,ac,nr,nc,cnt+1,temp)
#             if iswin:
#                 winner.append(turn)
#             else:
#                 loser.append(turn)
#     if flag:
#         if winner:
#             return (0,min(winner))
#         else:
#             return (1,max(loser))
#     else:
#         return (1,cnt)


# def solution(board, aloc, bloc):
#     ar,ac,br,bc = aloc[0],aloc[1],bloc[0],bloc[1]
#     answer = A_turn(ar,ac,br,bc,0,board)[1]
#     return answer