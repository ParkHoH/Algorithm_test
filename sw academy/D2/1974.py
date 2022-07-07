TC = int(input())
for t in range(1, TC + 1):
    graph = []
    for _ in range(9):
        graph.append(list(map(int, input().split())))

    result = 1
    # 정사각형 검증
    for i in range(0, 9, 3):
        stop = False
        for j in range(0, 9, 3):
            num = 0
            for k in range(3):
                num += sum(graph[i+k][j:j+3])
    
            if num != 45:
                result = 0
                stop = True
                break
        
        if stop: break

    # 가로 방향 검증
    if not stop:
        for i in range(9):
            num = sum(graph[i])
            if num != 45:
                result = 0
                stop = True
                break
    
    # 세로 방향 검증
    if not stop:
        for j in range(9):
            num = 0
            for i in range(9):
                num += graph[i][j]

            if num != 45:
                result = 0
                stop = True
                break

    print(f'#{t} {result}')