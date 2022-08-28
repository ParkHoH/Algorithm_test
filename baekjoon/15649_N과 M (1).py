# 직접 구현
def permutation(cnt):
    if cnt == M:
        for i in selected:
            print(i, end=" ")
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            selected[cnt] = i+1
            permutation(cnt+1)
            visited[i] = False

N, M = map(int, input().split())
visited = [False] * N
selected = [0] * M
permutation(0)


# 라이브러리 사용
from itertools import permutations

N, M = map(int, input().split())
for permu in permutations(range(1, N+1), M):
    print(*list(permu))