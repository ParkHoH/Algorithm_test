N, K = map(int, input().split())
L = [i for i in range(1, N+1)]
location = -1

print("<", end="")
while L:
    location = (location + K) % len(L)
    if len(L) == 1:
        print(L.pop(location), end="")
    else:
        print(L.pop(location), end=", ")
    location -= 1

print(">", end="")