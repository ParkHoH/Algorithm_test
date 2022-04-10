from collections import deque

def solution(n, results):
    lower = [[] for _ in range(n+1)]
    higher = [[] for _ in range(n+1)]
    for a, b in results:
        lower[a].append(b)
        higher[b].append(a)
        
    def bfs(i, arr):
        queue = deque()
        queue.append(i)
        cnt = 0
        L = []
        while queue:
            i = queue.popleft()
            for node in arr[i]:
                if node not in L:
                    queue.append(node)
                    L.append(node)
                    cnt += 1
        return cnt

    result = 0
    for i in range(1, n+1):
        if bfs(i, lower) + bfs(i, higher) + 1 == n:
            result +=1
    return result

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))