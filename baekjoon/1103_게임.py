from collections import deque
import sys
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]

def check_possible():
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    queue = deque()
    queue.append((0, 0, 0)) # x, y, dist

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

    return False

