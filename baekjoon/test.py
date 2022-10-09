N = 5
selected = [0] * (N)
visited = [False] * N

def combination(cnt, start):
    if cnt == N:
        print(selected)
        return

    for i in range(start, N):
        selected[cnt] = i
        combination(cnt+1, i+1)

def permutation(cnt):
    if cnt == N:
        print(selected)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            selected[cnt] = i
            permutation(cnt+1)
            visited[i] = False

combination(0, 0)
print("-----")
permutation(0)