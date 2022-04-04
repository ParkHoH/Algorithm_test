def solution(rows, columns, queries):
    graph = [[i+1 + j*columns for i in range(columns)] for j in range(rows)]
    result = []
    for query in queries:
        changed_list = []
        y1, x1, y2, x2 = query
        y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1
        ori_num = graph[y1][x1]

        for x in range(x1, x2):
            changed_num = graph[y1][x+1]
            graph[y1][x+1] = ori_num
            changed_list.append(ori_num)
            ori_num = changed_num

        for y in range(y1, y2):
            changed_num = graph[y+1][x2]
            graph[y+1][x2] = ori_num
            changed_list.append(ori_num)
            ori_num = changed_num

        for x in range(x2, x1, -1):
            changed_num = graph[y2][x-1]
            graph[y2][x-1] = ori_num
            changed_list.append(ori_num)
            ori_num = changed_num

        for y in range(y2, y1, -1):
            changed_num = graph[y-1][x1]
            graph[y-1][x1] = ori_num
            changed_list.append(ori_num)
            ori_num = changed_num
                
        result.append(min(changed_list))
    return result

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))