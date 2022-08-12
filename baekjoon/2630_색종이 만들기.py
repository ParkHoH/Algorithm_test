N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

blue = 0
white = 0

def dfs(startX, endX, startY, endY, n):
    global blue
    global white
    standard = graph[startX][startY]

    if n == 1:
        if standard == 1:
            blue += 1
        else:
            white += 1
        return

    impossible = False

    for i in range(startX, endX):
        for j in range(startY, endY):
            if graph[i][j] != standard:
                impossible = True
                break
    
    if impossible:
        half_n = n//2
        dfs(startX, startX+half_n, startY, startY+half_n, half_n)
        dfs(endX-half_n, endX, startY, startY+half_n, half_n)
        dfs(startX, startX+half_n, endY-half_n, endY, half_n)
        dfs(endX-half_n, endX, endY-half_n, endY, half_n)
    else:
        if standard == 1:
            blue += 1
        else:
            white += 1

dfs(0, N, 0, N, N)
print(white)
print(blue)