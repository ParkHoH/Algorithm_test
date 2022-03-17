# deque solution
from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    result = 0
    for city in cities:
        if cacheSize == 0:
            result += 5
        elif city.lower() in cache:
            cache.remove(city.lower())
            cache.append(city.lower())
            result += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city.lower())
            result += 5
    return result

# another solution
def solution(cacheSize, cities):
    cache = []
    result = 0
    for city in cities:
        if cacheSize == 0:
            result += 5
        elif city.lower() in cache:
            cache.remove(city.lower())
            cache.append(city.lower())
            result += 1
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city.lower())
            result += 5
    return result

print(solution(0,["Jeju", "Pangyo", "NewYork", "newyork"]))