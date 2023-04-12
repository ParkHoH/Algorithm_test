dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
direction = {
    "N": 0,
    "S": 1,
    "W": 2,
    "E": 3,
}

def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                cur = [i, j]
                break
    
    MAX_X, MAX_Y = len(park)-1, len(park[0])-1

    for route in routes:
        op, n = route.split()
        n = int(n)

        # 주어진 방향으로 이동할 때 공원을 벗어나는 경우,
        if not 0 <= cur[0] + n*dx[direction[op]] <= MAX_X or not 0 <= cur[1] + n*dy[direction[op]] <= MAX_Y:
            continue

        stop = False
        
        # 주어진 방향으로 이동 중 장애물을 만나는 경우,
        for i in range(1, n+1):
            
            new_x = cur[0] + i*dx[direction[op]]
            new_y = cur[1] + i*dy[direction[op]]

            if park[new_x][new_y] == "X":
                stop = True
                break
        
        if not stop:
            cur = [new_x, new_y]

    return cur


print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
print(solution(	["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))
print(solution(	["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))