dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]    

def dfs(x, y, cnt, place, visited):
    cnt += 1
    visited[x][y] = True
    if cnt == 3:
        return True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 5 or nx < 0 or ny >= 5 or ny < 0:
            continue
        if visited[nx][ny] == False:
            if place[nx][ny] == "P":
                return False
            if place[nx][ny] == "O":
                if not dfs(nx, ny, cnt, place, visited):
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        stop = False
        for x in range(5):
            for y in range(5):
                if place[x][y] == "P":
                    visited = [[False] * 5 for _ in range(5)]
                    if not dfs(x, y, 0, place, visited):
                        stop = True
                        break
            if stop:
                break
        if stop:
            answer.append(0)
        else:
            answer.append(1)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))