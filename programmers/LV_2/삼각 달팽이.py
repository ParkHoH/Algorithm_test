# def solution(n):
#     result = [[0]*(i+1) for i in range(n)]
#     dx = [1, 0, -1]
#     dy = [0, 1, -1]
#     flag = 0
#     x, y = -1, 0
#     count = 1
#     while n:
#         for _ in range(n):
#             x += dx[flag]
#             y += dy[flag]
#             result[x][y] = count
#             count += 1

#         if flag == 0:
#             flag = 1
#         elif flag == 1:
#             flag = 2
#         else:
#             flag = 0
#         n -= 1
    
#     answer = []
#     for arr in result:
#         answer += arr
#     return answer

def solution(n):
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    b = [[0] * i for i in range(1, n+1)]
    x = y = 0
    num = 1
    d = 0
    while num <= (n+1)*n // 2:
        b[y][x] = num
        ny = y + dy[d]
        nx = x + dx[d]
        num += 1
        if (0 <= ny < n) and (0 <= nx <= ny) and (b[ny][nx] == 0):
            y, x = ny, nx
        else:
            d = (d+1) % 3
            y += dy[d]
            x += dx[d]
            
    return sum(b)

print(solution(5))