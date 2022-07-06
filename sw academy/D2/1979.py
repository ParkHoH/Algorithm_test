TC = int(input())
for t in range(1, TC + 1):
    N, K = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    result = 0
    # 가로
    for i in range(N):
        num = 0
        for j in range(N):
            if graph[i][j] == 0:
                num = 0
            else:
                num += 1

            if num == K:
                if j+1 < N and graph[i][j+1] == 1:
                    continue
                result += 1

    # 세로
    for j in range(N):
        num = 0
        for i in range(N):
            if graph[i][j] == 0:
                num = 0
            else:
                num += 1

            if num == K:
                if i+1 < N and graph[i+1][j] == 1:
                    continue
                result += 1

    print(f'#{t} {result}')