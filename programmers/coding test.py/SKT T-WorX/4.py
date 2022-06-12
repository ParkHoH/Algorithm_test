import sys
from copy import deepcopy
sys.setrecursionlimit(10**6)

def solution(grid, k):
    result = [float('inf')]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    # dfs로 (1, 1) -> (n, m)의 모든 경로 탐색
    def dfs(x, y, possible_cnt, camping_cnt, visited):
        # 목표 지점에 도착했을 때 기존 result와 비교
        if x == len(grid)-1 and y == len(grid[0])-1:
            result[0] = min(result[0], camping_cnt)
            return

        visited[x][y] = True
        # 평지에서 캠핑함. 단, 캠핑 필요 없는 경우 제외.
        if possible_cnt != k and grid[x][y] == "." and result[0] > camping_cnt+1:
            dfs(x, y, k, camping_cnt+1, deepcopy(visited))

        # 움직일 수 없는 경우 스킵
        if possible_cnt == 0:
            return

        # 4방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # grid의 범위를 벗어나는 경우 스킵
            if nx >= len(grid) or ny >= len(grid[0]) or nx < 0 or ny < 0:
                continue
            
            # 강이거나 이미 방문한 경우 스킵
            if grid[nx][ny] == "#" or visited[nx][ny]:
                continue
            
            # 숲이더라도 움직일 수 있는 횟수가 1이고 목적지가 아닌 경우 스킵
            if grid[nx][ny] == "F" and possible_cnt == 1 and nx != len(grid)-1 and ny != len(grid[0])-1:
                continue

            dfs(nx, ny, possible_cnt-1, camping_cnt, deepcopy(visited))

    dfs(0, 0, k, 0, visited)
    return result[0]

print(solution(["..FF", "###F", "###."], 4))
print(solution(["..FF", "###F", "###."], 5))
print(solution([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 6))
