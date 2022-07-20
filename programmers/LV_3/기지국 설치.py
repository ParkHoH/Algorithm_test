def solution(n, stations, w):
    result = 0
    num = w * 2 + 1
    front = 1
    end = stations[0] - w
    
    for i in range(len(stations)):
        if front >= end:
            if i != len(stations) - 1:
                front = stations[i] + w + 1
                end = stations[i+1] - w
            continue
        
        result += (end - front) // num + 1
        if (end - front) % num == 0:
            result -= 1
        
        if i == len(stations) - 1:
            continue

        front = stations[i] + w + 1
        end = stations[i+1] - w
    
    if n > stations[-1] + w :
        result += (n - (stations[-1] + w)) // num + 1
        if (n - (stations[-1] + w)) % num == 0:
            result -= 1
        
    return result


import math

def solution(n, stations, w):
    num = 2 * w + 1
    location = 1
    result = 0
    for station in stations:
        result += max(math.ceil((station - location - w) / num), 0)
        location = station + w + 1
        
    if n >= location:
        result += math.ceil((n - location + 1) / num)
    
    return result