from collections import deque

def solution(n, computers):
    visited = [False] * n
    
    def bfs(i):
        queue = deque()
        queue.append(i)
        visited[i] = True
        while queue:
            i = queue.popleft()
            for idx in range(len(computers[i])):
                if computers[i][idx] == 1 and visited[idx] == False:
                    visited[idx] = True
                    queue.append(idx)
    
    cnt = 0
    for i in range(n):
        if visited[i] == False:
            cnt += 1
            bfs(i)
    return cnt

print(solution(	3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))