def solution(n, times):
    left, right = 0, max(times)*n
    while left < right:
        mid = (left + right) // 2
        cnt_people = 0
        for time in times:
            cnt_people += mid // time
            if cnt_people >= n:
                break
                
        if cnt_people >= n:
            right = mid
        else:
            left = mid + 1
    return left


# 시간 초과
# import heapq

# def solution(n, times):
#     cnt = result = 0
#     time_heaq = []
#     for time in times:
#         heapq.heappush(time_heaq, (time, time))
#     while cnt != n:
#         time_complited, time_cost = heapq.heappop(time_heaq)
#         heapq.heappush(time_heaq, (time_complited+time_cost, time_cost))
#         cnt += 1
#         result = time_complited
#     return result

print(solution(6,[10, 7]))