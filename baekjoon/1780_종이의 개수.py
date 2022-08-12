import sys
input = sys.stdin.readline

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

minus = zero = plus = 0

def dfs(x, y, n):
    global minus, zero, plus
    standard = graph[x][y]

    if n == 1:
        if standard == -1:
            minus += 1
        elif standard == 0:
            zero += 1
        else:
            plus += 1
        return

    impossible = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != standard:
                impossible = True
                break

        if impossible:
            break

    if impossible:
        dn = n//3
        for i in range(3):
            for j in range(3):
                dfs(x + dn*i, y + dn*j, dn)
    
    else:
        if standard == -1:
            minus += 1
        elif standard == 0:
            zero += 1
        else:
            plus += 1

dfs(0, 0, N)
print(minus)
print(zero)
print(plus)