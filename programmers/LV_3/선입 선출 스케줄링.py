def solution(n, cores):
    if n <= len(cores):
        return n
    
    n -= len(cores)
    start = 1
    end = max(cores) * n
    while start < end:
        mid = (start + end) // 2
        capacity = 0
        for core in cores:
            capacity += mid // core
        
        if capacity >= n:
            right = mid
        else:
            start = mid + 1
            
    return right


# wrong solution
# import heapq

# def solution(n, cores):
#     heap = []
#     num = min(n, len(cores))
#     for i in range(num):
#         heapq.heappush(heap, [cores[i], i])
    
#     while heap:
#         cnt, idx = heapq.heappop(heap)
#         if num != n:
#             num += 1
#             heapq.heappush(heap, [cnt + cores[idx], idx])
            
#     return idx + 1

print(solution(	6, [1, 2, 3]))