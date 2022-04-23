from collections import deque

def solution(info, edges):
    # 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립
    result_sheep, result_wolf = 1, 0
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)
        
    queue = deque()
    queue.append([0, 1, 0])
    while queue:
        n, cnt_sheep, cnt_wolf = queue.popleft()
        for node in graph[n]:
            if info[node] == 0:
                result_wolf += 1
                queue.append([node, result_sheep, result_wolf])
            elif info[node] == 1:
                if result_sheep <= result_wolf+1:
                    continue
                else:
                    result_wolf += 1
                    queue.append([node, result_sheep, result_wolf])
            
    return result_sheep

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))