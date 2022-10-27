import heapq
import sys
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

M, N = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]

def dijkstra():
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    heap = []
    heap.append((0, 0, 0)) # 부순 벽, x, y

    while heap:
        cnt, x, y = heapq.heappop(heap)

        if x == N-1 and y == M-1:
            return cnt

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            heapq.heappush(heap, (cnt if board[nx][ny] == 0 else cnt+1, nx, ny))

print(dijkstra())