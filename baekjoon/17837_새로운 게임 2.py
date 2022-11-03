import sys
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)







# n, k = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# chess = [[[] for _ in range(n)] for _ in range(n)]

# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# horse = []
# cnt = 0

# for i in range(k):
#     x, y, d = map(int, input().split())
#     horse.append([x-1, y-1, d-1])
#     chess[x-1][y-1].append(i)


# def change_dir(d):
#     if d in [0, 2]:
#         d += 1
#     elif d in [1, 3]:
#         d -= 1
#     return d

# def solution(num):
#     x, y, d = horse[num]
#     nx = x + dx[d]
#     ny = y + dy[d]
#     if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
#         d = change_dir(d)
#         horse[num][2] = d
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
#             return True

#     horse_up = []
#     for h_idx, h_n in enumerate(chess[x][y]):
#         if h_n == num:
#             horse_up.extend(chess[x][y][h_idx:])
#             chess[x][y] = chess[x][y][:h_idx]
#             break

#     if board[nx][ny] == 1:
#         horse_up = horse_up[-1::-1]

#     for h in horse_up:
#         horse[h][0], horse[h][1] = nx, ny
#         chess[nx][ny].append(h)

#     if len(chess[nx][ny]) >= 4:
#         return False
#     return True

# while True:
#     what = False
#     if cnt > 1000:
#         print(-1)
#         break
    
#     for i in range(k):
#         if solution(i) == False:
#             what = True
#             break
#     cnt += 1
#     if what:
#         print(cnt)
#         break