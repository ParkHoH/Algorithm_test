from collections import deque

def chk_visited(x, time, ori_x):
    if checked[x][0]: # 이미 방문한 경우
        if checked[x][2] == time+1: # 방문 시간이 동일해야 함
            checked[x][1] += checked[ori_x][1]

    else: # 첫 방문인 경우
        checked[x][0] = True
        checked[x][1] = checked[ori_x][1]
        checked[x][2] = time+1
        queue.append([x, time+1])

N, K = map(int ,input().split())

checked = [[False, 1, 0] for _ in range(100001)] # 방문 여부, 누적 cnt, 시간 제한
checked[N][0] = True
queue = deque()
queue.append([N, 0])

while queue:
    x, time = queue.popleft()

    if x == K:
        break
    
    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx <= 100000:
            chk_visited(nx, time, x)

print(checked[K][2]) # 시간
print(checked[K][1]) # 방법의 수