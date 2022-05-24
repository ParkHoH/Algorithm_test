from itertools import combinations

N, M, H = map(int, input().split())
graph = [[0] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1 

L = []
for i in range(1, H+1):
    for j in range(1, N):
        if graph[i][j] != 1 and graph[i][j-1] != 1 and graph[i][j+1] != 1:
            L.append([i, j])

def check():
    for j in range(1, N+1):
        i = 1
        column = j
        while i != H+1:
            if graph[i][column-1] == 1:
                column -= 1
            elif graph[i][column] == 1:
                column += 1
            i += 1

        if column != j:
            return False
    
    return True

result = 0
impossible = True

while result != 4:
    if result == 0 and check():
        print(result)
        impossible = False
        break

    if result:
        for comb in combinations(L, result):
            for i, j in comb:
                graph[i][j] = 1

            if check():
                print(result)
                impossible = False
                break

            for i, j in comb:
                graph[i][j] = 0

    if not impossible:
        break    
    
    result += 1

if impossible:
    print(-1)