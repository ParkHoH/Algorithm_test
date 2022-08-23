import sys
input = sys.stdin.readline

N, L = map(int, input().split())
parent = [i for i in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(L):
    a, b = map(int, input().split())

    if cnt != N:
        if not visited[a]:
            visited[a] = True
            print("LADICA")

        elif not visited[b]:
            visited[b] = True
            print("LADICA")

        else:
            

    else:
        print("SMECE")
        
    