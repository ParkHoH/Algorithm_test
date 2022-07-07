TC = int(input())
for t in range(1, TC + 1):
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            num = 0
            for k in range(M):
                num += sum(graph[i+k][j:j+M])
            result = max(result, num)

    print(f'#{t} {result}')