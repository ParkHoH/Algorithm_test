from collections import deque

A, B = map(int, input().split())
dic = {}

queue = deque()
queue.append(A)
dic[A] = 1
result = -1
stop = False

while queue:
    x = queue.popleft()
    for nx in [2*x, int(str(x)+"1")]:
        if nx > B:
            continue

        elif nx == B:
            result = dic[x]+1
            stop = True
            break

        elif nx not in dic:
            queue.append(nx)
            dic[nx] = dic[x]+1

print(result)