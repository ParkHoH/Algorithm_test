from collections import deque

N = int(input())
queue = deque(range(1, N+1))
while len(queue) != 1:
    queue.popleft()
    num = queue.popleft()
    queue.append(num)

print(queue[0])