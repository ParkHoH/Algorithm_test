def solution(n):
    result = [[0]*(i+1) for i in range(n)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    direction = 0
    x, y = -1, 0
    count = 1
    while n:
        for _ in range(n):
            x += dx[direction]
            y += dy[direction]
            result[x][y] = count
            count += 1
        direction = (direction+1) % 3
        n -= 1
    
    return sum(result, [])

print(solution(5))