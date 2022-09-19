from collections import deque

n, m = map(int,input().split())
queue = deque([i for i in range(1,n+1)])
idx = list(map(int,input().split()))

result = 0
for num in idx:
    while True:
        if queue[0] == num:
            queue.popleft()
            break

        else:
            if queue.index(num) <= len(queue) // 2:
                queue.rotate(-1)
                result += 1

            else:
                queue.rotate(1)
                result += 1

print(result)