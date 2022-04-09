import heapq
from collections import deque

def solution(jobs):
    list_waiting = []
    time_complited = 0
    current_time = 0
    jobs_length = len(jobs)
    jobs.sort(reverse=True)
    while jobs or list_waiting:
        cnt = 0
        while jobs:
            if jobs[-1][0] <= current_time:
                heapq.heappush(list_waiting, jobs.pop()[::-1])
                cnt += 1
                if not jobs:
                    break
            else:
                if cnt != 0 or list_waiting:
                    break
                current_time = jobs[-1][0]
        
        time_required, time_request = heapq.heappop(list_waiting)
        current_time += time_required
        time_complited += current_time - time_request
    
    return time_complited // jobs_length

print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))