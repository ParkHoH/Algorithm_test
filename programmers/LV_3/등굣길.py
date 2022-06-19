def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]
    graph[0][0] = 1
        
    for i, j in puddles:
        graph[j-1][i-1] = "puddle"
    
    for i in range(n):
        for j in range(m):
            if i == j == 0 or  graph[i][j] == "puddle":
                continue
            
            if i-1 >= 0 and graph[i-1][j] != "puddle":
                a = graph[i-1][j]
            else:
                a = 0
            
            if j-1 >= 0 and graph[i][j-1] != "puddle":
                b = graph[i][j-1]
            else:
                b = 0
            
            graph[i][j] = (a + b) % 1000000007
    
    return graph[-1][-1]

print(solution(	4, 3, [[2, 2]]))