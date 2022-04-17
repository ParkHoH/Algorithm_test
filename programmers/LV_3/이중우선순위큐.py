import heapq

def solution(operations):
    min_heapq = []
    max_heapq = []
    for operation in operations:
        order, num = operation.split()
        if order == "I":
            heapq.heappush(min_heapq, int(num))
            heapq.heappush(max_heapq, -int(num))
        else:
            if min_heapq:
                if int(num) == 1:
                    max_value = heapq.heappop(max_heapq)
                    min_heapq.remove(-max_value)
                else:
                    min_value = heapq.heappop(min_heapq)
                    max_heapq.remove(-min_value)
    if min_heapq:
        return [-heapq.heappop(max_heapq), heapq.heappop(min_heapq)]
    else:
        return [0, 0]