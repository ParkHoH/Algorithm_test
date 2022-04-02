from collections import deque

def solution(progresses, speeds):
    queue = deque()
    for i in range(len(progresses)):
        queue.append([100-progresses[i], speeds[i], False])
        
    day = 0
    answer = []
    while queue:
        day += 1
        cnt = 0
        for progress in queue:
            if progress[2] == False:
                progress[0] -= progress[1]
            if progress[0] <= 0:
                progress[2] = True
        while len(queue) > 0 and queue[0][2] == True:
            queue.popleft()
            cnt += 1
        if cnt != 0:
            answer.append(cnt)
    return answer
            
        