from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    L = input().split()

    if L[0] == "push_front":
        queue.appendleft(L[1])

    elif L[0] == "push_back":
        queue.append(L[1])

    elif L[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif L[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)

    elif L[0] == "size":
        print(len(queue))

    elif L[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)

    elif L[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif L[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)