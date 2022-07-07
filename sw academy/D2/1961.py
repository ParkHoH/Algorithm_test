def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result

TC = int(input())
for t in range(1, TC + 1):
    N = int(input())
    result = [[] for _ in range(N)]
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    cnt = 0
    while cnt < 3:
        graph = rotate(graph)
        for i in range(N):
            if cnt < 2:
                result[i] += list(map(str, graph[i])) + [" "]
            else:
                result[i] += list(map(str, graph[i]))

        cnt += 1

    print(f'#{t}')
    for i in range(N):
        print(''.join(result[i]))