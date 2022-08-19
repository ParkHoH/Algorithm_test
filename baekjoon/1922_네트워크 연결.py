import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
costs = []

for _ in range(M):
    a, b, c = map(int, input().split())
    if a != b:
        costs.append([a, b, c])

costs.sort(key=lambda x: x[2])
connected = set()
connected.update([costs[0][0], costs[0][1]])
result = costs[0][2]

while len(connected) != N:
    for cost in costs:
        a, b, c = cost

        if a in connected and b in connected:
            continue

        if a in connected or b in connected:
            connected.update([a, b])
            result += c
            break

print(result)