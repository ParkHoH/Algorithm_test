from datetime import datetime
import time

def solution(lines):
    for i in range(len(lines)):
        date, hms, time_process = lines[i].split()
        time_mktime = time.mktime(datetime.strptime(date + hms.split('.')[0], "%Y-%m-%d%H:%M:%S").timetuple())
        ms = round(float('0.' + hms.split('.')[1]), 3)
        total_seconds = time_mktime + ms
        lines[i] = [total_seconds - round(float(time_process.split('s')[0]), 3) + 0.001, total_seconds]
    
    max_value = 1
    lines.sort(key=lambda x: x[1])
    for i in range(len(lines)):
        end_standard = lines[i][1]
        cnt = 1
        for j in range(i+1, len(lines)):
            start_target = lines[j][0]
            if start_target < end_standard + 1:
                cnt += 1
        max_value = max(max_value, cnt)
            
    return max_value
print(solution(	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))