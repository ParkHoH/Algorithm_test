# board를 탐색하며 모든 바이러스를 리스트에 넣어줌
# 0의 카운트가 필요함
# 조합을 이용해 첫 활성화 바이러스를 M개 골라줌
# 해당 바이러스 조합을 queue에 넣어주고 4방향 탐색
# 방문한 곳은 다시 방문하지 않음
# queue가 빌 때까지 반복하고 마지막 시간을 기존 최소 시간과 비교해서 갱신함

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

viruses = []
cnt_zero = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            cnt_zero += 1

        elif board[i][j] == 2:
            viruses.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    
    for x, y in combi:
        visited[x][y] = True
        queue.append([x, y, 0])

    cnt = 0
    
    while queue:
        x, y, time = queue.popleft()

        global result
        if time >= result:
            return 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] or board[nx][ny] == 1:
                continue
            
            if board[nx][ny] == 0:
                cnt += 1
            
            if cnt == cnt_zero:
                return time+1

            visited[nx][ny] = True
            queue.append([nx, ny, time+1])

    return 0

if cnt_zero != 0:
    result = float('inf')

    for combi in combinations(viruses, M):
        min_time = bfs()
        if min_time != 0:
            result = min(result, min_time)

else:
    result = 0

if result == float('inf'):
    print(-1)
else:
    print(result)