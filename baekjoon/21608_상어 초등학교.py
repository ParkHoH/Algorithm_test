# 시간복잡도: 400 * 4 * 400
# 해당 학생의 좌표를 넣어놓은 dict 필요
# 학생을 기록해놓는 board 
# dx, dy 필요

# 순서
# 학생을 순차 탐색하면서 해당 학생 방문 처리
# 좋아하는 학생 탐색하며 해당 학생이 앉았는지 확인
# 1) 앉아있지 않은 경우 board를 탐색하며 비어있는 칸이 최대로 되는 경우로 앉히기
# 2) 앉아있는 경우 해당 학생의 좌표를 확인하고 위, 왼쪽, 오른쪽, 아래 순으로 탐색하기

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

N = int(input())
N_square = N**2
prefers = [[] for _ in range(N_square+1)]
board = [[0] * N for _ in range(N)]
location = {}

for _ in range(N_square):
    idx, *prefer = map(int, input().split())
    prefer = set(prefer)
    prefers[idx] = prefer
    candidate = []

    for prefer_student in prefer:
        if prefer_student in location: # 자리 잡은 경우
            x, y = location[prefer_student]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny]:
                    continue

                candidate.append((nx, ny))

    if candidate: # 자리 잡은 경우
        max_prefer = -1
        max_blank = -1
        loca = (0, 0)
        
        for x, y in candidate:
            cnt_prefer = 0
            cnt_blank = 0

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                    
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if board[nx][ny] == 0:
                    cnt_blank += 1
                elif board[nx][ny] in prefer:
                    cnt_prefer += 1

            if max_prefer < cnt_prefer:
                max_prefer = cnt_prefer
                max_blank = cnt_blank
                loca = (x, y)
            
            elif max_prefer == cnt_prefer:
                if max_blank < cnt_blank:
                    max_blank = cnt_blank
                    loca = (x, y)

                elif max_blank == cnt_blank:
                    if loca[0] > x:
                        loca = (x, y)

                    elif loca[0] == x:
                        if loca[1] > y:
                            loca = (x, y)

    else: # 자리 잡지 않은 경우
        max_blank = -1
        loca = (0, 0)

        for x in range(N):
            for y in range(N):
                if board[x][y]: continue # 이 부분을 체크해주지 않아서 틀렸음
                cnt_blank = 0

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    
                    if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny]:
                        continue
                    
                    cnt_blank += 1

                if max_blank < cnt_blank:
                    max_blank = cnt_blank
                    loca = (x, y)
                    if max_blank == 4: break

    x, y = loca
    board[x][y] = idx
    location[idx] = (x, y)

answer = 0

for x in range(N):
    for y in range(N):
        idx = board[x][y]
        cnt_prefer = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
                    
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            
            if board[nx][ny] in prefers[idx]:
                cnt_prefer += 1

        if cnt_prefer:
            answer += 10 ** (cnt_prefer-1)

print(answer)