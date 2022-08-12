N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y, n):
    global first
    standard = graph[x][y]

    if n == 1:
        print(standard, end="")
        return
    
    impossible = False

    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] !=standard:
                impossible = True
        
        if impossible: break

    if impossible:
        first = False
        half_n = n//2
        print("(", end="")
        for i in range(2):
            for j in range(2):
                dfs(x + half_n*i, y + half_n*j, half_n)
        print(")", end="")

    else:
        print(standard, end="")

first = True
dfs(0, 0, N)