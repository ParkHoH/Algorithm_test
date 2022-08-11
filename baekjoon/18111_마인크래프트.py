N, M, B = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

max_value = 0
min_value = float('inf')
for i in range(N):
    for j in range(M):
        max_value = max(max_value, graph[i][j])
        min_value = min(min_value, graph[i][j])

result = [float('inf'), 0] # 시간, 땅 높이

for height in range(min_value, max_value+1):
    time = cnt = 0
    for i in range(N):
        for j in range(M):
            num = graph[i][j] # num에 넣어주지 않고 직접 접근하는 경우가 많아지면 효율성에서 통과하지 못함
            if num < height:
                time += height - num
                cnt += height - num
            elif num > height:
                time += 2 * (num - height)
                cnt -= num - height

    if cnt <= B and result[0] >= time:
        result = [time, height]

for i in result:
    print(i, end=" ")