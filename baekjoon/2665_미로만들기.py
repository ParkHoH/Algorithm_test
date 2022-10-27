import heapq
import sys
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]

def dijkstra():
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True

    heap = []
    heap.append((0, 0, 0)) # 바꾼 블록 수, x좌표, y좌표

    while heap:
        cnt, x, y = heapq.heappop(heap)

        if x == N-1 and y == N-1:
            return cnt

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            heapq.heappush(heap, (cnt if board[nx][ny] == 1 else cnt+1, nx, ny))

    return 0

print(dijkstra())