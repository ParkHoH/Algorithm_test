import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx, cnt):
    next = students[idx]

    if checked[next][0]:
        global result
        if next not in route:
            result += cnt+1

        elif cnt != 0:
            result += checked[next][1]

    else:
        checked[next][0] = True
        checked[next][1] = cnt+1
        route.add(next)
        dfs(next, cnt+1)

T = int(input())

for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))

    result = 0
    checked = [[False, 0] for _ in range(n+1)]

    for i in range(1, n+1):
        if not checked[i][0]:
            checked[i][0] = True
            route = set()
            route.add(i)
            dfs(i, 0)

    print(result)