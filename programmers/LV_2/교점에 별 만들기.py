from itertools import combinations

def solution(line):
    lines_combination = list(combinations(line, 2))
    stars = []
    for line_1, line_2 in lines_combination:
        A, B, E = line_1
        C, D, F = line_2
        if A*D == B*C:
            continue
        x = (B*F - E*D) / (A*D - B*C)
        y = (E*C - A*F) / (A*D - B*C)
        if x == int(x) and y == int(y):
            stars.append([int(x), int(y)])

    max_x, min_x = max(star[0] for star in stars), min(star[0] for star in stars)
    max_y, min_y = max(star[1] for star in stars), min(star[1] for star in stars)
    graph = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for x, y in stars:
        graph[y - min_y][x - min_x] = '*'
    
    result = list(map(''.join, graph))
    result.reverse()
    return result

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))