from collections import Counter, deque

def solution(n, works):
    list_works = deque(sorted(Counter(works).items(), reverse=True))
    while n > 0:
        key, cnt = list_works[0]
        if key == 0:
            break
        if n >= cnt:
            if len(list_works) > 1 and list_works[1][0] == key-1:
                list_works.popleft()
                list_works[0] = (key-1, list_works[0][1] + cnt)
            else:
                list_works[0] = (key-1, cnt)
            n -= cnt
        else:
            list_works[0] = (key, cnt - n)
            if len(list_works) > 1 and list_works[1][0] == key-1:
                list_works[1] = (key-1, list_works[1][1] + n)
            else:
                list_works.append((key-1, n))
            break
            
    result = 0
    for num, cnt in list_works:
        result += (num**2) * cnt
    return result

# other solution
from heapq import heapify, heappush, heappop

def solution(n, works):
    heapify(works := [-i for i in works])
    for _ in range(min(n, abs(sum(works)))):
        heappush(works, heappop(works)+1)
    return sum([i*i for i in works])

print(solution(4, [4, 3, 3]))