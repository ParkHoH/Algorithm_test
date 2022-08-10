from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ori_queue = deque(range(1, n+1))
pop_queue = []
L = []

for _ in range(n):
    L.append(int(input()))

num = 0
impossible = False
s = ""

for i in range(n):
    if impossible:
        break

    if not pop_queue:
        pop_queue.append(ori_queue.popleft())
        s += "+\n"

    if pop_queue[-1] > L[i]:
        impossible = True
        break
    elif pop_queue[-1] < L[i]:
        while True:
            if not ori_queue:
                impossible = True
                break

            pop_queue.append(ori_queue.popleft())
            s += "+\n"
            if pop_queue[-1] > L[i]:
                impossible = True
                break
            elif pop_queue[-1] == L[i]:
                pop_queue.pop()
                s += "-\n"
                break
    else:
        pop_queue.pop()
        s += "-\n"

if impossible:
    print("NO")
else:
    print(s)