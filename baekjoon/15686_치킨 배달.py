from itertools import combinations

N, M = map(int, input().split())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if L[i][j] == 2:
            chicken.append((i, j))
        elif L[i][j] == 1:
            house.append((i, j))

result = []
for comb in combinations(chicken, M):
    distance = 0
    for h_x, h_y in house:
        min_dist = float('inf')
        for c_x, c_y in comb:
            if abs(h_x - c_x) + abs(h_y - c_y) < min_dist:
                min_dist = abs(h_x - c_x) + abs(h_y - c_y)
        distance += min_dist
    result.append(distance)

print(min(result))