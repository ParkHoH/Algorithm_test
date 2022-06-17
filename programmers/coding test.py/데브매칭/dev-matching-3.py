def solution(n, edges, k, a, b):

    graph = [[] for i in range(n)]
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    set_result = set()
    def bfs(location, cnt, visited, road):
        visited[location] = True
        if cnt > k:
            return
        if location == b:
            for i in road:
                set_result.add(i)
            return

        for end in graph[location]:
            if visited[end] == False:
                road.append((location, end))
                cnt += 1
                bfs(end, cnt, visited[:], road[:])
                cnt -= 1
                road.pop()
                visited[end] = False

    bfs(a, 0, [False]*n, [])
    count = 0
    set_result = list(set_result)
    for i in range(len(set_result)):
        for j in range(i+1, len(set_result)):
            if set_result[i][0] == set_result[j][1] and set_result[i][1] == set_result[j][0]:
                count += 1

    return len(set_result) - count


print(solution(8,[[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]],4,0,3))