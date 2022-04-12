from collections import deque

def solution(n, t, m, timetable):
    bus_timetable = [540 + i*t for i in range(n)]
    for idx, time in enumerate(timetable):
        h, mm = map(int, time.split(":"))
        timetable[idx] = h*60 + mm
    timetable.sort()
    timetable = deque(timetable)
    
    for idx, time in enumerate(bus_timetable):
        last_time = 0
        cnt = 0
        while timetable and timetable[0] <= time and cnt != m:
            last_time = timetable.popleft()
            cnt += 1
        
        if idx == len(bus_timetable)-1:
            answer = last_time-1 if cnt == m else time
                
    return str(answer//60).rjust(2, "0") + ":" + str(answer%60).rjust(2, "0")

print(solution(	2, 10, 2, ["09:10", "09:09", "08:00"]))