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