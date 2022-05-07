def solution(queue1, queue2):
    queue = queue1 + queue2
    average = sum(queue) / 2
    if average != int(average):
        return -1

    result = float('inf')
    start = 0
    end = len(queue1) - 1
    sum_queue = sum(queue1)
    while start < len(queue):
        if sum_queue == average:
            result = min(result, start + end - (len(queue1)-1))

        if sum_queue < average:
            if end == len(queue)-1:
                break
            end += 1
            sum_queue += queue[end]
        else:
            start += 1
            sum_queue -= queue[start-1]

    if result < float('inf'):
        return result
    return -1
    
print(solution([1, 2, 1, 2]	,[1, 10, 1, 2]))



# def solution(queue1, queue2):
#     queue = queue1 + queue2
#     average = sum(queue) / 2
#     if average != int(average):
#         return -1

#     result = []
#     start = end = 0
#     sum_queue = queue[end]
#     while start < len(queue):
#         if sum_queue == average:
#             result.append((start, end))

#         if sum_queue < average:
#             if end == len(queue)-1:
#                 break
#             end += 1
#             sum_queue += queue[end]
#         else:
#             start += 1
#             sum_queue -= queue[start-1]

#     return result