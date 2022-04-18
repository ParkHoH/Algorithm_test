def solution(routes):
    routes.sort()
    result = 1
    start, end = routes[0]
    for i in range(1, len(routes)):
        if routes[i][0] in range(start, end+1) or routes[i][1] in range(start, end+1):
            start = max(start, routes[i][0])
            end = min(end, routes[i][1])
        else:
            start, end = routes[i]
            result += 1
    return result

print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))