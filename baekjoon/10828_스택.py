import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    L = input().split()

    if L[0] == "push":
        stack.append(L[1])

    elif L[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif L[0] == "size":
        print(len(stack))

    elif L[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif L[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)