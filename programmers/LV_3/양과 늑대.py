def solution(info, edges):
    visited = [False] * len(info)
    visited[0] = True
    global result
    result = 0

    def dfs(cntSheep, cntWolf, visited):
        if cntSheep <= cntWolf:
            return

        global result
        result = max(result, cntSheep)

        for parent, child in edges:
            isWolf = info[child]

            if visited[parent] and not visited[child]:
                visited[child] = True
                dfs(cntSheep + (isWolf == 0), cntWolf + (isWolf == 1), visited) # 새롭게 알게 된 부분
                visited[child] = False
    
    dfs(1, 0, visited)
    return result


from copy import deepcopy

def solution(info, edges):
    graph = [[] for _ in range(len(info))]

    for parent, child in edges:
        graph[parent].append(child)
        
    global max_sheep
    max_sheep = 0
    
    def dfs(n, cnt_sheep, cnt_wolf, connected):
        if cnt_sheep <= cnt_wolf:
            return

        global max_sheep
        max_sheep = max(max_sheep, cnt_sheep)
        
        for i in connected:
            copy_connected = deepcopy(connected)
            copy_connected.remove(i)
            for j in graph[i]:
                copy_connected.add(j)

            if info[i] == 0:
                dfs(n, cnt_sheep+1, cnt_wolf, copy_connected)
            else:
                dfs(n, cnt_sheep, cnt_wolf+1, copy_connected)
        
    connected = set()

    for i in graph[0]:
        connected.add(i)

    dfs(0, 1, 0, connected)
    return max_sheep

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
